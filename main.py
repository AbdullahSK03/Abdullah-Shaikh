from flask import Flask, render_template
import requests as REQ





app = Flask(__name__)
api = REQ.get("https://api.npoint.io/a790dc67973030cc7f94").json


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Qualification')
def content():
        return render_template("content.html", api=api)

@app.route('/Contact')
def contact():
    return render_template("contact.html")


if "__main__" == __name__:
    app.run(debug=True)