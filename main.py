from flask import Flask, render_template
from mlbdata.schedule import fetchData

app = Flask(__name__)

games = fetchData()

@app.route('/')
def index():
    return render_template('index.html')

app.debug = True
app.run()