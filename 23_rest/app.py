from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating

from urllib import request
import json


key = "dpf7J5K33dTVC0xYPZzQVrgy5z3eiwqnTKraBvd4"

app = Flask(__name__)

url = f"https://api.nasa.gov/planetary/apod?api_key={key}&count=1"

with request.urlopen(url) as response:
    response = response.read().decode('utf-8')

    print(response)
    
json.dumps(response)


@app.route("/")
def index():
    return render_template( 'index.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

