import re
import math

with open('book_hw1.txt', 'r', encoding = 'utf-8') as f:
    dict = {}
    c = 1
    for lines in f:
        lines1 = re.sub("—","",lines)
        lines1 = lines1.lower()
        
        lines1 = lines1.replace(",","")
        lines1 = lines1.replace(".","")
        lines1 = lines1.replace("!","")
        lines1 = lines1.replace("?","")
        lines1 = lines1.replace("(","")
        lines1 = lines1.replace(")","")
        lines1 = lines1.replace("«","")
        lines1 = lines1.replace("»","")
        lines1 = lines1.replace(":","")
        lines1 = lines1.replace(";","")
        
        
        
        l = lines1.split()
        for i in range(len(l)):
            new = {l[i]: [c, i+1]}
            dict.update(new)
        c+=1    

a = str(input('First word?'))
b = str(input('Second word?'))


k = 0
w = 0
while w < len(dict):
    
    for i in dict:
        w+=1
        if a == i:
            defin_a = dict[i][0]
            defin_a = int(defin_a)
            for j in dict:
                if b == j:
                    defin_b = dict[j][0]
                    defin_b = int(defin_b)
                    if abs(defin_a - defin_b) == 1:
                        print('yes, in neighbour abzats')
                        k = 1
                    if abs(defin_a - defin_b) == 0:
                        print('in one abzats, way =' , abs(int(dict[j][1]) - int(dict[i][1])))
if k == 0:
    print('no, not in neighbour abzats')


''' 
list_for_a = []
list_for_b = []
for i in dict:
    if a == i:
        print(i)
        list_for_a.append(dict[i][0])
        print(list_for_a)
for j in dict:
    if b == j:
        list_for_b.append(dict[j][0])

k = 0
for s in range(len(list_for_a)):
    for t in range(len(list_for_b)):
        if abs(int(s)-int(t)) == 1:
            print('yes')
            k = 1
    
if k == 0:
    print('no')

print(list_for_a,list_for_b)
'''
        
