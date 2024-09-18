'''
Will Nzeuton
Topher Lovers
SoftDev
K05 -- File parsing
2024-09-17
time spent: 0.3
'''
import random
def parseDuckies(file_name):
    
    file = open(file_name, "r")
    line = file.read()
    
    
    line = line.replace('\n', '')
    people = line.split('@@@')
    
    dividedPeople = []
    
    for i in range(len(people) - 1):
        dividedPeople.append(people[i].split('$$$'))
    
    return dividedPeople
    
def DDArrayToDict(arr):
    my_dict = {}
    for i in arr:
        if(i[0] not in my_dict.keys()):
            my_dict[i[0]] = []
        my_dict[i[0]].append([i[0], i[1], i[2]])
    return my_dict

krewes = DDArrayToDict(parseDuckies("krewes.txt"))

def gen_rand_student():
    rand_period = list(krewes.keys())[random.randint(0, len(krewes) - 1)]
    #generate a random period
    rand_devo = krewes[rand_period][random.randint(0, len(krewes[rand_period]) - 1)]
    #generate devo from said period    
    return rand_devo

student = gen_rand_student()

print(f"Found {student[1]} and {student[2]} from period {student[0]}")
