import os
import re
import random

data = []
dic = {}
path = "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts\c"


for file in os.listdir(path):
    data.append(open(path+"\\"+file, encoding='utf-8').read().replace('\n', '').replace('\'', ''))
    words = ''.join(data)
    words = re.split(r'\s+', words)

for i in range(len(words)-2): #or else out of bounds from wordafter
    key = str(words[i]) + " " + str(words[i+1]) #grabs both key words
    wordafter = words[i+2]

    if key not in dic:
        dic[key] = [(wordafter, 1)]# puts it in
        
    else:
        flag = True
        for values in range(len(dic[key])):
            if wordafter == dic[key][values][0]: #if value is already in key, add 1 
                dic[key][values] = (dic[key][values][0], dic[key][values][1]+1)
                #flag variable to check if i get a match inside the loop
                flag = False
        if flag:
            dic[key] = dic[key] + [(wordafter, 1)]


""" Random key """
ran = random.choice(list(dic.keys()))
values = ()
count = 0

while count < 1000:
    tickets = [] #new ticket system
    for values in dic[ran]:
        #pick a random value associated with the key
        tickets = tickets+([values[0]]*values[1])
        
    ran = ran.split()[-1] + ' ' + random.choice(tickets)
    print(ran)
    count += 1

        
    
    

