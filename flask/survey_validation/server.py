from flask import Flask, session, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "hello"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1 or len(request.form['comment'])<1:
        flash("Name cannot be blank")
        flash("Comment cannot be blank")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("A comment cannot have more than 120 characters")
        return redirect('/')
    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)