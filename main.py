from flask import Flask, render_template



app = Flask(__name__)

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
    