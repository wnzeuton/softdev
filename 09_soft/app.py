
from flask import Flask
app = Flask(__name__)          

TNPG = "What departure"
roster = "Will, Tim, Danny"
import csv, random
occ_dict = {}
with open('occupations.csv', newline='') as csvfile:

    read = csv.reader(csvfile)
    
    last = 0
    for row in read:
        if(row[0] == 'Total'):
            total = eval(row[1])
        elif(row[0] != 'Occupation' and row[0] != 'Job Class'):
            occ_dict[row[0]] = [last, eval(row[1]) + last]
            last = eval(row[1]) + last
            #print(row)
#print(occ_dict)
#print(total)

#for item in .
#print(occ_dict['Business and Financial operations'])
#print(rand)
def get_rand():
    rand = random.uniform(0, total)
    for job in occ_dict.keys():
        #print(job)
        #print(occ_dict[job][1])
        if(rand - occ_dict[job][1] <= 0):
            return job
@app.route("/")                
def hello_world():
    print(__name__)            
    return f"{TNPG}: {roster} <br><br> {list(occ_dict)} <br><br> Chose: {get_rand()}"    
app.run(debug=True)                      
                
