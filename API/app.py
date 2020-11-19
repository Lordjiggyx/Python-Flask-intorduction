#Starting Point Of application

#Importing flask
import flask

#importoing jsonify & request
from flask import jsonify, request

#Instantiating flask
app = flask.Flask(__name__)


# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


#annotatation for route
@app.route("/")
def home():
    return """<h1>Reading Archive<h1>
    <p>Prototype API for science fiction novels<p>
    """


#annotatation for route
@app.route("/api/books")
def get_All():
    #Jsonify converts collections to JSON format 
    return jsonify(books)

@app.route("/api/getid")
def get_by_id():
    #Check to see if an ID was part if the URL
    if "id" in request.args:
        #creates a local variable reefering to whatever was passed into the id
        id = int(request.args['id'])
    else:
        return "ERROR please specify an id"

    #creating an empty list
    result = []

    #loop through data and match result that fit the requested id
    for book in books:
        if book['id']==id:
            result.append(book)


    #return the results using jsonify
    return jsonify(result)

@app.route("/api/updateid")
def update_by_id():
    #Check to see if an ID or author was part if the URL
    if "id" and "author" in request.args:
        #creates a local variable reefering to whatever was passed into the id
        id = int(request.args['id'])
        #Author is also obtained
        author = (request.args['author'])
    else:
        return "ERROR please specify an id"

    #creating an empty list
    result = []

    print(author)
    #loop through data and match result that fit the requested id
    for book in books:
        if book['id']==id:
            #Author details change must  be single quotes
            book['author'] = author

    
    #return the results using jsonify
    return "Book has been updated"

@app.route("/api/removeid")
def remove_by_id():
    #Check to see if an ID was part if the URL
    if "id"  in request.args:
        #creates a local variable reefering to whatever was passed into the id
        id = int(request.args['id'])
        
    else:
        return "ERROR please specify an id"

    #creating an empty list
    result = []

    #loop through data and match result that fit the requested id
    for book in books:
        if book['id']==id:
            #Author details change must  be single quotes
            books.remove(book)

    
    #return the results using jsonify
    return "Book has been removed"    
    
app.run(debug=True)