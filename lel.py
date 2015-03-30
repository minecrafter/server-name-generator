import random
import os
from flask import Flask, render_template, abort

lists = {}

for list in os.listdir('lists'):
  words = []
  with open('lists/' + list) as f:
    for l in f:
      line = l.strip().title()
      if line != '' and '\\' not in line and ',' not in line and not line.startswith('#'):
        words.append(line)

  lists[list] = words

suffix = ['MC', ' Cloud', 'Cloud', ' Network', 'Network', 'PVP', ' PVP', 'Craft', 'Block', 'Mine', 'Factions',
          ' Factions', 'Prison', ' Prison', 'Survival', ' Survival', ' Minigames', 'Anarchy', 'Hardcore',
          'Gaming', ' Gaming', 'Game']

app = Flask(__name__)

@app.route('/generate/<type>')
def generate_name(type):
  if type not in lists:
    abort(404)
  return random.choice(lists[type]) + random.choice(suffix)

@app.route('/<type>')
def list(type):
  if type not in lists:
    abort(404)
  return render_template('index.html', type=type)

@app.route('/')
def index():
  return render_template('index.html', type="latin-derived")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
