from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask import requests as REQ
# import smtplib


# api = REQ.get("https://api.quotable.io/random").json()
app = Flask(__name__)



'''srno, p, h, image'''

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Qualification', methods=['GET'])
def content():
        
        

        return render_template("content.html")

@app.route('/Contact')
def contact():
    return render_template("contact.html")

@app.route('/Services')
def services():
     return render_template("services.html")


#send email



if "__main__" == __name__:
    app.run(debug=True)