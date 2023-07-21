from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests as REQ
import smtplib


api = REQ.get("https://api.quotable.io/random").json()
app = Flask(__name__)

print(api)


'''srno, p, h, image'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/portfolio_web'
db=SQLAlchemy(app)


class Data:
    def __init__(self, srno, p, h, image):
        self.srno = srno
        self.p = p
        self.h = h
        self.image = image

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Qualification')
def content():
        return render_template("content.html")

@app.route('/Contact')
def contact():
    return render_template("contact.html")

@app.route('/Services')
def services():
     return render_template("services.html")

if "__main__" == __name__:
    app.run(debug=True)