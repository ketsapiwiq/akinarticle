table: spare matrix? (is that possible in a database?)
colums are objects
rows are questions

each cell:
	weighting between question and object, 
	
decide which question to ask
-like the entrpoy function, look at probable objects and pick question such that the objects get split in half on yes or no

end of the thing (and wrong): add question or object
	if right: increase question weights for that object
	if wrong, add a person
		if already in the database, what do you do?
		if not in database, add a column for that person with default values based on the question path

then you learn...

table will have totals at the bottom to make search linear, then only the totals will be modified


when we start a game, we need to initialize a dictionary that will store the current weight for each object in the game {object: current_value}
OR: PRIORITY QUEUE/HEAP

functions:

update_weights(object,questions, values) DONE
update_data DONE
add_object(name) DONEISH
add_question(question) DONEISH
ask_question()
guess()

IN MEMORY:
STORE QUESTION PATH AND ANSWERS

AFTER PROGRAM GUESSES:
if wrong:
    decrease weights for that object on those questions
    CONTINUE STORING SO THAT THEY CAN BE INCREASED FOR EVENTUAL RIGHTNESS
    offer option: continue? or teach the program?
if right:
    increase
    

RENAME VALUE COLUMN IN DATA TO WEIGHT

half weights are positive and half are negative

sum of positives and negatives?
    heap: good way of organizing
    priority queue based on entropy
    define a comparable function
    
    compute entropies on the fly?
    IF NOT:
        store entropies with question - whenever you change anything with the question, store the weight
            e.g. store positives and negatives
