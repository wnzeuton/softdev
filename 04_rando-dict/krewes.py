#Will Nzeuton
#Topher Lovers
#SoftDev
#K04 -- Random Generation from Dictionary
#2024-09-13
#time spent: 0.2
import random
#Define dictionary of students with SoftDev period as key and list of students as value
krewes = {
           4: [ 
		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
		],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

def gen_rand_student():
    rand_period = list(krewes.keys())[random.randint(0, len(krewes) - 1)]
    #generate a random period
    rand_devo = krewes[rand_period][random.randint(0, len(krewes[rand_period]) - 1)]
    #generate devo from said period    
    return rand_devo

def test():
    print(gen_rand_student())
