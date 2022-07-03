from flask import Flask, render_template
from mlbdata.schedule import fetchData

app = Flask(__name__)

@app.route('/')
def index():
    games = fetchData()
    return render_template('index.html', games=games)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run()