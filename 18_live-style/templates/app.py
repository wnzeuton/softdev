

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

from flask import session

import os
#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)


@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    if 'username' not in session.keys():
        return render_template( 'login.html' )
    else:
        return response()
@app.route("/response", methods=['GET', 'POST'])
def response():
    if('username' not in session.keys()):
        session['username'] = request.args['username']
    return render_template('response.html', user = session['username'], meth = request.method) 

@app.route("/logout")
def logout():
    session.pop('username')
    return render_template('logout.html')

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

