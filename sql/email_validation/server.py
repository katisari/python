from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnect import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = connectToMySQL('email_list')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    session['emails'] = mysql.query_db("SELECT * FROM emails;")
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        for round in session['emails']:
            if round['email'] == request.form['email']:
                flash("The email is already taken")
                return redirect('/')
            else:
                flash(f"The email address you entered {request.form['email']} is a VALID email address! Thank you")
                query = "INSERT INTO emails (email, created_at) VALUES(%(emails)s, NOW());"
                data = {"emails": request.form['email']}
                mysql.query_db(query, data)
                return redirect('/success')
@app.route('/success')
def success():
    query = "SELECT email, DATE_FORMAT(created_at, '%m/%d/%y %h:%i%p') AS created_at FROM emails;"
    session['emails'] = mysql.query_db(query)
    return render_template("success.html")




if __name__ == "__main__":
    app.run(debug=True)