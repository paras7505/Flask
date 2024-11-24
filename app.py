from flask import Flask,request,render_template
from markupsafe import escape
from models import Products,Form
from database import session

app = Flask(__name__)


@app.route('/')
def homePage():
    add_product()
    return render_template('homePage.html')


@app.route('/products/')
def products():
    return render_template('products.html')


@app.route('/hello/')
@app.route('/hello/<name>/')
def greet(name=None):
    return render_template('greet.html' , name = name)


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
        age = request.form.get('age')
        email = request.form.get('email')
        address = request.form.get('address')
        user_details()
        print(request.form)
    else:
        firstName = request.args.get('fname')
        lastName = request.args.get('lname')
        print(request.form)
    
    return f"{firstName} {lastName} {age} {email} {address}"



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


def add_product():
    product = Products(name = 'hello' , price = 20 , quantity = 20)
    session.add(product)
    session.commit()

def user_details():
    details = Form(Firstname = '' , Lastname = "" , age = '', email = '' , Address = '')
    session.add(details)
    session.commit()


