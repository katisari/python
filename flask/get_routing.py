from flask import Flask, render_template, request
app=Flask(__name__)
print(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hi " + name.title()

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    return (word + "\n") * int(num)


if __name__ == "__main__":
    app.run(debug=True)
