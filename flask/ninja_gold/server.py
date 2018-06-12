import random
import datetime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsKey"
@app.route('/')
def index():
    if 'total_gold' in session:
        print("hello")

    else:
        session['total_gold'] = 0
    if 'activity' in session:
        print("activity here")
    else:
        session['activity']=[]
        print(type(session['activity']))
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['building'] == "farm":
        money = random.randrange(10, 21)
        session['total_gold'] += money
        time = str(datetime.datetime.now())
        print(time)
        text = "Earned " + str(money) + " golds from the farm! " + time 
        print(text)
        session['activity'].append(["gr", text])
    elif request.form['building'] == "cave":
        money = random.randrange(5, 11)
        time=str(datetime.datetime.now())
        session['total_gold'] += money
        text = "Earned " + str(money) + " golds from the cave! " + time 
        session['activity'].append(["gr", text])
    elif request.form['building'] == "house":
        money = random.randrange(2, 6)
        time = str(datetime.datetime.now())
        session['total_gold'] += money
        text = "Earned " + str(money) + " golds from the house! " + time 
        session['activity'].append(["gr", text])
    elif request.form['building'] == "casino":
        money = random.randrange(-50, 51)
        time = str(datetime.datetime.now())
        session['total_gold'] += money
        text = "Entered a casino and " + str(money) + " golds " + time 
        if money >= 0:
            session['activity'].append(["gr", text])
        else:
            session['activity'].append(["rd", text])
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
