'''
Will Nzeuton
Blue Stuff
K06: Parsing CSV files
2024-09-18
time-spent:
'''
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
    
def test(n):
    freq_dict = {}
    total = 0
    for i in range(n):
        total += 0
        job = get_rand()
        if(job in freq_dict.keys()):
            freq_dict[job] += 1
        else:
            freq_dict[job] = 1

    return freq_dict
print(test(100000))
    