from flask import Flask,request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> main page </p>"


@app.route("/products/")
def product():
    return "<p> product page </p>"

@app.route("/products/aboutUs/")
def aboutUs():
    return "<ul><li>Coffee</li><li>Tea</li><li>Milk</li></ul>"


# catching variable

@app.route("/product/variable/<string:name>/")
def variable_catching(name):
    return f" <p> hello world {escape(name)} </p> "


@app.route("/user/<username>/")
def user(username):
    return f"<p> username:#{escape(username)}</p>"

@app.route("/path/<path:subpath>")
def path(subpath):
    return f"<p> path:{escape(subpath)}</p>"


# methods get, post etc

@app.route("/methods/" , methods =['GET', 'POST'])
def method():
    if request.method == 'POST':        
        return "<p> post method </p>"
    else:
        return "<p> get method </p> "



@app.route("/methods/getting/" , methods = ['POST','GET','PUT', 'OPTIONS','PATCH', 'HEAD','DELETE'])
def meth():
    if request.method == 'DELETE':
        return "<p> hello post method </p>"re
    else:
        return "<p> hello get method </p>"

