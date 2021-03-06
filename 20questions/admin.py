#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
    admin.py
    
    Andy Freeland and Dan Levy
    5 June 2010
    
    Provides administrative functions, such as retraining characters and deleting
    objects and characters. Accessed at the /admin url. Laughably insecure.
'''

import web
import config, model

import twentyquestions as game
import re, base64

urls = (
    '', 'admin',
    '/', 'admin',
    '/dq', 'delete_question',
    '/do', 'delete_object',
    '/data', 'data',
    '/retrain/(\d+)', 'retrain',
    '/login', 'login'
)

render = web.template.render('templates', base='base')
app = web.application(urls, locals())

# def logged_in():
#     if web.ctx.env.get('HTTP_AUTHORIZATION') is not None:
#         web.session.loggedin=True
#         return True
#     else:
#         raise web.seeother('/login')
#         return False

class admin:
    def GET(self):
        '''Renders the admin page, presenting a menu of administrative functions.'''
        # if logged_in():
        return render.admin()


class delete_question:
    def GET(self):
        '''Lists all of the questions so that selected questions can be deleted.'''
        # login_required()
        questions = model.get_questions()

        return render.delete_question(questions)


    def POST(self):
        '''Deletes selected questions and returns to the admin page.'''
        # login_required()
        question_ids = web.input()
        for id in question_ids:
            model.delete_question(id)
        raise web.seeother('/')

class delete_object:
    def GET(self):
        # login_required()
        '''Lists all of the objects so that selected objects can be deleted.'''
        objects = model.get_objects()
        return render.delete_object(objects)
    def POST(self):
        # login_required()
        '''Deletes selected objects. and returns to the admin page.'''
        object_ids = web.input()
        for id in object_ids:
            model.delete_object(id)
        raise web.seeother('/')
        
class data:
    def GET(self):
        '''Renders a page listing all of the objects so that they can be retrained.'''
        objects = model.get_objects()
        return render.data(list(objects))

class retrain:
    def GET(self, object_id):
        '''Renders a page with all of the questions and values for a specified
           object_id so that it can be retrained manually.'''
        object = model.get_object_by_id(object_id)
        if object:
            weighted_questions_for_object = model.get_weighted_questions_for_object_id(object_id)

            return render.retrain(object, weighted_questions_for_object)
        else:
            raise web.seeother('/') # returns to admin page
            
    def POST(self, object_id):
        '''Updates object_id with the newly selected answers to questions.'''
        inputs = web.input()
        for question_id in inputs:
            answer = inputs[question_id]
            if answer in ['yes','no']:
                value = eval('game.' + answer) * game.RETRAIN_SCALE # STRONGLY weights values learned this way
                model.update_data(object_id, question_id, value)
        
        raise web.seeother('/data')
