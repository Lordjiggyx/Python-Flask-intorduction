#Starting Point Of application

#Importing flask
import flask

#Instantiating flask
app = flask.Flask(__name__)

#annotatation for route
@app.route("/")
def home():
    return "Hello you ran your first appliaction"

app.run(debug=True)