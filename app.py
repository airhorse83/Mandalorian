from flask import Flask, render_template

from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/About')
def about():
    return render_template("About.html")
    
@app.route('/Menu')
def menu():
    return render_template("Menu.html")

@app.route('/Contact')
def contact():
    return render_template("Contact.html")


if __name__ == '__main__':
    app.debug = True
    app.run()    