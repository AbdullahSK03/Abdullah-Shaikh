from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

@app.route('/content')
def index():
    return render_template('content.html')

if __name__ == '__main__':
    app.run(debug=True)