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
                query = "SELECT * FROM users WHERE email=%(email)s"
                outcome = mysql.query_db(query, data)
                session['userid'] = outcome[0]['id']
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
    session['user_info'] = mysql.query_db("SELECT * FROM users")


    query = "SELECT messages.id AS message_id, users.name as sender, messages.content, receiver.name AS receiver, receiver.id as receiver_id, messages.created_at AS sent_at, CONCAT(FLOOR(HOUR(TIMEDIFF(NOW(), messages.created_at)) / 24), ' days ', MOD(HOUR(TIMEDIFF(NOW(), messages.created_at)), 24), ' hours ', MINUTE(TIMEDIFF(NOW(), messages.created_at)), ' minutes') AS how_long_ago FROM users JOIN messages ON users.id = messages.user_id JOIN users as receiver ON receiver.id = messages.friend_id WHERE receiver.id = %(receiver_id)s;"
    data = {
        'receiver_id': str(session['userid'])
    }
    results = mysql.query_db(query, data)
    counter = 0
    if results:
        for result in results:
            counter += 1
    session['joined_query'] = results
    print(counter)
    print(results)
    return render_template("welcome.html", results = results, counter=counter)
@app.route('/logoff', methods=['POST'])
def logoff():
    session.clear()
    return redirect('/')
@app.route('/sendmessage/<id>', methods=['POST'])
def sendmessage(id):
    flash("Message Sent")
    query = "INSERT INTO messages (content, user_id, friend_id, created_at) VALUES (%(content)s, %(user_id)s, %(receiver_id)s, NOW())"
    data = {
        'content' : request.form['comment'],
        'user_id' : session['userid'],
        'receiver_id' : id
    }
    mysql.query_db(query, data)
    return redirect('/success')

@app.route('/danger/<receiver_id>/<message_id>')
def delete(receiver_id, message_id):
    if session['joined_query']:
        for row in session['joined_query']:
            if row['message_id']:
                if int(session['userid']) ==  int(receiver_id):
                    query = "DELETE FROM messages WHERE id = %(mesg_id)s;"
                    data = {
                        'mesg_id': message_id
                    }
                    mysql.query_db(query, data)
                    flash("Message successfully deleted")
                    return redirect('/success')
    ip_ad = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  
    session.clear()       
    return render_template("danger.html", message_id = str(message_id), ip_ad = ip_ad)


if __name__ == "__main__":
    app.run(debug=True)