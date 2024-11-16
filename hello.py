from flask import Flask,request,render_template
from markupsafe import escape

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p> main page </p>"


# @app.route("/products/")
# def product():
#     return "<p> product page </p>"

# @app.route("/products/aboutUs/")
# def aboutUs():
#     return "<ul><li>Coffee</li><li>Tea</li><li>Milk</li></ul>"


# # catching variable

# @app.route("/product/variable/<string:name>/")
# def variable_catching(name):
#     return f" <p> hello world {escape(name)} </p> "


# @app.route("/user/<username>/")
# def user(username):
#     return f"<p> username:#{escape(username)}</p>"

# @app.route("/path/<path:subpath>")
# def path(subpath):
#     return f"<p> path:{escape(subpath)}</p>"


# # methods get, post etc

# @app.route("/methods/" , methods =['GET', 'POST'])
# def method():
#     if request.method == 'POST':        
#         return "<p> post method </p>"
#     else:
#         return "<p> get method </p> "



# @app.route("/methods/getting/" , methods = ['POST','GET','PUT', 'OPTIONS','PATCH', 'HEAD','DELETE'])
# def meth():
#     if request.method == 'DELETE':
#         return "<p> hello post method </p>"
#     else:
#         return "<p> hello get method </p>"


@app.route('/')
def homePage():
    return render_template('homePage.html')


@app.route('/products/')
def products():
    return render_template('products.html')


@app.route('/hello/')
@app.route('/hello/<name>/')
def greet(name=None):
    return render_template('greet.html' , name = name)



@app.route('/lists/')
def listt():
    fruits = ['mango' , 'watermelon']
    return render_template('list.html', fruits = fruits) 


#  for get method 
@app.get("/form/")
def form():
    FirstName = request.args.get('fname')
    LastName = request.args.get('lname', default="")
    print(request.args)
    return f"<h1> user details {FirstName} {LastName} </h1>"


#  for post method
@app.post('/form/')
def form_details():
    firstName = request.form['fname']
    lastName = request.form['lname']
    print(request.form)    
    return f"<h1> user details in post method {firstName} {lastName} </h1>"
             
#  using if else 


@app.route('/ifelse/', methods=['POST', 'GET'])
def forms():
    if request.method == 'POST':       
        firstName = request.form.get('fname')
        lastName = request.form.get('lname')
        print(request.form)
    else:
        firstName = request.args.get('fname')
        lastName = request.args.get('lname')
        print(request.form)
    
    return f"First name {firstName} {lastName}"



# chatgpt code 

@app.route('/ifelsee/', methods=['POST', 'GET'])
def formss():
    if request.method == 'POST':    
        firstName = request.form.get('fname', '')
        lastName = request.form.get('lname', '')
        print("POST data:", request.form)
    else:
        firstName = request.args.get('fname', '')
        lastName = request.args.get('lname', '')
        print("GET data:", request.args)
    
    return f"First Name: {firstName}, Last Name: {lastName}"

