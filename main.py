from flask import Flask, render_template
from mlbdata.schedule import fetchData

app = Flask(__name__)

@app.route('/')
def index():
    games = fetchData()
    return render_template('index.html', games=games)

app.debug = True
app.run()