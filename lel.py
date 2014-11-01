import random
from flask import Flask, render_template

latin = []
with open('list.txt') as f:
    for l in f:
        line = l.strip().title()
        if line != '' and '\\' not in line and ',' not in line:
            latin.append(line)

suffix = ['MC', ' Cloud', 'Cloud', ' Network', 'Network', 'PVP', ' PVP', 'Craft', 'Block', 'Mine', 'Factions', ' Factions']

app = Flask(__name__)

@app.route('/generate')
def generate_name():
    return random.choice(latin) + random.choice(suffix)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
