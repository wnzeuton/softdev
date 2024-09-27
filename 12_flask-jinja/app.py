# Clyde 'Thluffy' Sinclair
# SoftDev
# Sep 2024

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
We will get an error because we use render_template later in the script

Q1:
Yes, http://127.0.0.1:5000/my_foist_template


Q2:
Which file we want to use as a template - replaces mention of foo in template with provided string - replaces collection variable in template with coll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"
coll = [0,1,1,2,3,5,8]
chant = [["WE ARE STRONG","WE BELONG","HEAR OUR SONG", "WE MARCH ALONG"], ["WE WONT FALL", "WE GIVE OUR ALL", "HEED OUR CALL", "WE WONT STALL"]]
gallery = ["topher.jpeg", "topher2.png", "topher3.png"]
res = ["https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.stuycs.org/faculty/&ved=2ahUKEwjgmYH0ueOIAxX8FVkFHUYmJLUQFnoECBQQAQ&usg=AOvVaw0HkCpt-9OhSNnE2UfQcw6A","https://www.google.com/url?sa=i&url=https%3A%2F%2Fcestlaz.github.io%2Fposts%2F2013-10-31-halloween%2F&psig=AOvVaw1DS6i-3DPNCCN8NVU7AA4Y&ust=1727536752383000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCLCVkYa244gDFQAAAAAdAAAAABAE"]   
art = []
with open('static/art.txt', 'r') as art:
    lines = [x.replace('\n', '') for x in art.readlines()]
    art = lines
    print(lines)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)
@app.route("/topher")
def toph():
    return render_template('topher_tmplt.html', foo = "TOPHER LOVERS HOME", collection=chant, images = gallery, art = art, resources = res)

if __name__ == "__main__":
    app.debug = True
    app.run()
