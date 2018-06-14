from flask import Flask, render_template, redirect, session, request, flash
import re
from mysqlconnect import connectToMySQL
from flask_bcrypt import Bcrypt   

app = Flask(__name__)        
bcrypt = Bcrypt(app)
app.secret_key = "Hello"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = connectToMySQL('email_list')

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/register', methods=['POST'])
def process():
    results = mysql.query_db("SELECT * from users;")
    if len(request.form['name'])< 2:
        flash("Name cannot be blank", 'name')
    elif not request.form['name'].isalpha():
        flash("Please put correct name", 'name')
    if len(request.form['email'])< 1:
        flash("Email cannot be blank", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    if len(request.form['password'])<8 or len(request.form['confirm_pass'])<8:
        flash('Passwords needs to be at least 8 characters', 'password')
    elif request.form['password'] != request.form['confirm_pass']:
        flash("Passwords do not match", 'password')
    if '_flashes' in session.keys():
        return redirect('/')
    else:
        for result in results:
            if result['email'] == request.form['email']:
                flash("The email is already taken", 'email')
                return redirect('/')
            else:
                pw_hash = bcrypt.generate_password_hash(request.form['password'])
                query = "INSERT INTO users (email, name, password) VALUES (%(email)s, %(name)s, %(password)s);"
                data = {'name': request.form['name'],
                    'email': request.form['email'],
                    'password': pw_hash
                }
                mysql.query_db(query, data)
                session["name"] = request.form['name']
                return redirect("/success")
@app.route('/login', methods=['POST'])
def login():
    query = "SELECT * FROM users WHERE email = %(email)s"
    if len(request.form['email']) < 1 or len(request.form['password']) < 1:
        flash("Please complete all fields.")
        return redirect('/')
    data = {"email": request.form['email']}
    results = mysql.query_db(query, data)
    if results:
        if bcrypt.check_password_hash(results[0]['password'], request.form['password']):
            # if we get True after checking the password, we may put the user id in session
            session['userid'] = results[0]['id']
            session['name'] = results[0]['name']
            # never render on a post, always redirect!
            return redirect('/success')
    # if we didn't find anything in the database by searching by username or if the passwords don't match,
    # flash an error message and redirect back to a safe route
    flash("You could not be logged in.")
    return redirect('/')
@app.route('/success')
def success():
    return render_template("welcome.html")
@app.route('/logoff', methods=['POST'])
def logoff():
    session.clear()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)