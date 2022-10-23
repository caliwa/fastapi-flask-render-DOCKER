from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    url = 'http://fast-api/frutas'
    response = requests.get(url)
    response_json = json.loads(response.text)
    return render_template('index.html', context=response_json)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)