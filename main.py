from flask import Flask, render_template, req
# from flask_sqlalchemy import SQLAlchemy
from flask import requests as REQ
import smtplib


app = Flask(__name__)
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
with connection.login('abdhuzyfa@gmail.com', 'zaupklzasocwfvgs') as smtp:
    smtp.sendmail('abdhuzyfa@gmail.com',f'{REQ.form["email"]} {REQ.form["message"]}', msg = f'from: {REQ.form["email"]}\nto: {REQ.form["email"]}\nsubject: {REQ.form["subject"]}\n\n{REQ.form["message"]}')



'''srno, p, h, image'''

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Qualification')
def content():    
        return render_template("content.html")

@app.route('/Services')
def services():
     return render_template("services.html")


#send email



if "__main__" == __name__:
    app.run(debug=True)