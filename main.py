from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests as REQ



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/portfolio_web"
# db = SQLAlchemy(app)

# class Data(db.Model):
#     id = db.srno(db.Integer, primary_key=True)
#     img = db.p(db.St(100), nullable=False)
#     h = db.h(db.String(100), nullable=False)
#     p = db.image(db.String(100), nullable=False)




@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Qualification')
def content():
        return render_template("content.html", api=api)

@app.route('/Contact')
def contact():
    return render_template("contact.html")

@app.route('/Services')
def services():
     return render_template("services.html")

if "__main__" == __name__:
    app.run(debug=True)