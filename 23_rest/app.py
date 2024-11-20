from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating

from urllib import request
import json


key = "dpf7J5K33dTVC0xYPZzQVrgy5z3eiwqnTKraBvd4"

app = Flask(__name__)




@app.route("/")
def index():
    url = f"https://api.nasa.gov/planetary/apod?api_key={key}&count=1"

    with request.urlopen(url) as response:
        response = response.read().decode('utf-8')

        jsonify = json.loads(response)[0]
        
    print(jsonify)
    return render_template( 'index.html', date = jsonify['date'], description = jsonify['explanation'], title = jsonify['title'], url = jsonify['url'])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

