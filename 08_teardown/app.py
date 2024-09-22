'''
Will Nzeuton
Topher Lovers
SoftDev
K08 -- Applications using Flask
2024-09-22
time spent: 0.2
'''
'''
DISCO:
<note any discoveries you made here... no matter how small!>
It allows you to keep inputting into the terminal seemingly forever.
If you go to a web browser and put in the address that Flask outputs then it will run the app and then print __name__ to terminal and the page will display the result of hello_world()
It will reprint __name__ if you refresh the web browser
When you stop the application and refresh the page, there will be an error.
QCC:
0. I have seen similar syntax in Python (__init__). This is slightly reminiscent of instantiating an object in Java using a constructor
1. / could be the root of our directory, it could also be the root of a website (as in https://)
2. This will print to  the terminal
3. It will print "__main__"
4. Yes, this appears on the locally hosted web address: http://127.0.0.1 on the default port 5000 | I know because part of the original message says where the app is running
5. This looks like a Java method
 ...

INVESTIGATIVE APPROACH:
First navigated in our computer directories. 
When we found nothing we put the print statement outside of the function to figure out 
what we were to be looking for.
Once we paid closer attention to the Flask message and went to the web address we found more answers.
'''


from flask import Flask
app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?
app.run()                                # Q5: Where have you seen similar constructs in other languages?



