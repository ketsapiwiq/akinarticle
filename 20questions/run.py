#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
    webinterface.py
    
    Andy Freeland and Dan Levy
    5 June 2010
    
    Web interface to the twenty questions game. Each page/url is represented by
    a class. Uses the web.py library from http://webpy.org. Stores user data in
    a sesssion. HTML pages are stored in the templates directory, while static
    files such as CSS and fonts are stored in the static directory.
'''

import web
import config
import model
import twentyquestions as game
import admin

from urllib import quote
import bleach

import sys
sys.dont_write_bytecode = True


urls = (
    '/', 'index',
    '/begin', 'begin',
    '/answer/(\d+)', 'answer',
    '/guess', 'guess',
    '/guess/(\d+)', 'guess',
    '/learn', 'learn',
    '/restart', 'restart',
    '/admin', admin.app
)

app = web.application(urls, globals())
render = web.template.render('templates', base='base')

session_vars = {'count': 1, 'asked_questions': {},
                'initial_questions': [], 'objects_values': {}}
session = web.session.Session(app, web.session.DiskStore(
    'sessions'), initializer=session_vars)


def reset_game():
    '''Kills the session.'''
    session.kill()


class index:
    def GET(self):
        '''Shows the index page and asks the questions.'''

        if config.DISPLAY_CANDIDATES:  # clean up this section somehow
            nearby_objects_values = game.get_nearby_objects_values(
                session.objects_values, how_many=config.how_many_candidates)
        else:
            nearby_objects_values = None

        if not(session.get('asked_questions')) and not(session.get('initial_questions')):
            question = 'begin'
        else:
            question = game.choose_question(
                session.initial_questions, session.objects_values, session.asked_questions)
            if(nearby_objects_values):
                if(nearby_objects_values[0][0] >= config.answer_score_threshold):
                    raise web.seeother('/guess')

            if (question == None or session.count > config.how_many_questions):
                raise web.seeother('/guess')
        return render.index(question, session.get('count'), nearby_objects_values)


class begin:
    def POST(self):
        '''Initializes the session and returns to the index.'''

        session.initial_questions = game.load_initial_questions()
        session.objects_values = game.load_objects_values()

        raise web.seeother('/')


class restart:
    def POST(self):
        '''Restarts the game.'''
        reset_game()
        raise web.seeother('/')


class answer:
    def POST(self, question_id):
        '''Updates the local knowledgebase with the answer given to the question_id.'''

        question_id = int(question_id)  # otherwise it's unicode
        a = web.input().answer
        if a in ['yes', 'no', 'unsure']:
            answer = eval('game.' + a)
        else:
            answer = game.unsure
            # Should we increment even if unsure?
        if answer != game.unsure:
            session.count += 1
        game.update_local_knowledgebase(
            session.objects_values, session.asked_questions, question_id, answer)
        raise web.seeother('/')


class guess:
    def GET(self, chosen_id=None):
        '''Displays the computer's guess of who the user is thinking of.'''
        chosen = game.guess(session.objects_values)
        return render.guess(chosen)

    def POST(self, chosen_id=None):
        '''Learns whether the guess was correct or not. If 'yes', learn and restart.
           If 'no', go to 'learn' to learn a new character.'''
        a = web.input().answer

        if not(chosen_id):
            chosen_id = 1

        if a in ['no', 'teach me']:
            raise web.seeother('/learn')
        elif a in ['yes']:
            game.learn(session.asked_questions, int(chosen_id))

            reset_game()

            raise web.seeother('/')


class learn:
    def GET(self):
        '''Renders the learn page, allowing the user to select the correct character
           and add a new question.'''
        nearby_objects = game.get_nearby_objects(
            session.objects_values, how_many=config.how_many_candidates)
        return render.learn(nearby_objects)

    def POST(self):
        '''Processes the learning form and learns the correct character and new
           question.'''

        inputs = web.input()

        name = inputs.get('name')
        if name == "new":
            name = bleach.clean(inputs.get('new_article'))

        link = inputs.get('link')
        if link == "new":
            link = quote(inputs.get('new_link'), safe='/:?&#')

        question = bleach.clean(inputs.get('question', ''))
        if question:
            new_question_answer = inputs.get('new_question_answer')
            if new_question_answer in ['yes', 'no', 'unsure']:
                answer = eval('game.' + new_question_answer) * \
                    game.NEW_QUESTION_SCALE
                # strongly weights new answer
            else:
                answer = game.unsure

        if question.strip() != '' and not(model.get_question_by_text(question.strip())):
            # makes sure the question is not already in the database
            new_question_id = model.add_question(question)
        else:
            new_question = model.get_question_by_text(question.strip())
            # if question already in DB, returns question. else returns None.
            if new_question:
                new_question_id = new_question.id
            else:
                new_question_id = None

        if name and link:
            new_object_id = game.learn_article(session.asked_questions, name, link)
        else:
            new_object_id = None

        if new_question_id and new_object_id:
            model.update_data(new_object_id, new_question_id, answer)

        reset_game()
        # resets game data and starts a new game

        raise web.seeother('/')


if __name__ == '__main__':
    '''Runs the app.'''
    if web.config.debug:
        app.internalerror = web.debugerror
    app.run()
