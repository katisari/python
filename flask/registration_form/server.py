from flask import Flask, render_template, redirect, session, flash, request
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "yes"
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def process():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm_password']= request.form['confirm_password']
    print(request.form)
    if len(session['first_name'])<1 or len(session['last_name'])<1 or len(session['first_name'])<1 or len(session['email'])<1 or len(session['password'])<1 or len(session['confirm_password']) < 1:
        flash("All fields are required and must not be blank")
    elif session['first_name'].isdigit() or session['last_name'].isdigit():
        flash('First and Last Name cannot contain any numbers')
    elif len(session['password']) <= 8:
        flash('Password should be more than 8 characters')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif session['password'] != session['confirm_password']:
        flash("Password and Password Confirmation should match")   
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)