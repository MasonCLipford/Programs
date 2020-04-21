import random
import re
from tkinter import *

path = "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts\point_training.txt"
path2 = "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python37_64\\Scripts\\new_data.txt"

data = []
data.append(open(path, encoding='utf-8').read().replace('\n', ' '))
words = ''.join(data)
words = re.split(r'\s+', words)

i = 0
split = []
while i < len(words):
    split.append(words[i:i+3])
    i+= 3
print(split)


#set w1, w2, and b to a ran value between -1 and 1
weight1 = random.uniform(-1, 1)
weight2 = random.uniform(-1, 1)
bias = random.uniform(-1, 1)
learning = .2
weights = []

""" Training """
for i in range(len(split)-2):
    
    x = split[i][0]
    y = split[i][1]
    label = split[i][2]
    
    #computers w1x + w2y + b if ouput is greater than 0, it output as 1, else 0
    if weight1*float(x)+weight2*float(y)+bias > 0:
        percep = 1
    else:
        percep = 0

    #difference between correct label and output
    delta = abs(float(label)-float(percep))
    #w1=w1+x*delta*r
    weight1 = float(weight1) + float(x) * float(delta) * float(learning)
    #w2=w2+y*delta*r
    weight2 = float(weight2) + float(y) * float(delta) * float(learning)
    #bias=delta*r
    bias = float(delta) * float(learning)
    weights.append([weight1, weight2, bias])

data2 = []
data2.append(open(path2, encoding='utf-8').read().replace('\n', ' '))
words2 = ''.join(data2)
words2 = re.split(r'\s+', words2)

j = 0
split2 = []
while j < len(words2):
    split2.append(words2[j:j+2])
    j+= 2
print(split2)

root = Tk()
canvas = Canvas(width=600, height=600, bg='white')
canvas.grid()
canvas.create_line(0, (2.405*-20+7.493)*-15+300,600, (2.405*20+7.493)*-15+300, width=3, fill='red')


""" Percep Testing """
for i in range(len(split2)-1):
    for j in range(len(weights)):

        x = float(split2[i][0])
        y = float(split2[i][1])

        weight1 = float(weights[j][0])
        weight2 = float(weights[j][1])
        bias = float(weights[j][2])

        if weight1*x+weight2*y+bias > 0:
            canvas.create_oval(15*x+300-5, -15*y+300-5, 15*x+300+10-5, -15*y+300+10-5, fill='white')
            
        else:
            canvas.create_oval(15*x+300-5, -15*y+300-5, 15*x+300+10-5, -15*y+300+10-5, fill='black')






    
        




