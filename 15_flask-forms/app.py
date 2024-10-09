

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )

@app.route("/response", methods=['GET', 'POST'])
def response():
    return render_template('response.html', user = request.args['username'], meth = request.method) 


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

