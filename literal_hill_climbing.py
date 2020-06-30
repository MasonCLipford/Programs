from tkinter import *
from random import *
from time import sleep
from math import exp

def hill_climb(start):
    v = start
    last = start
    while True:
        N = [n for n in [v-1,v+1] if 0<=n<99]
        h = max([(height[n]-height[v],n) for n in N])
        print(v, N, h)
        if h[0] <= 0:
            return v
        else:
            v = h[1]
            canvas.create_rectangle(6*last, (height[last]-mid)*scale+300, 6*last+5, (height[last]-mid)*scale+300+5, fill='white')
            canvas.create_rectangle(6*v, (height[v]-mid)*scale+300, 6*v+5, (height[v]-mid)*scale+300+5, fill='green')
            canvas.update()
            sleep(1)
            last = v


def anneal(start):
    temp = 100
    num_iter = 1000
    stop_temp = 1

    v = start
    last = start

    while temp > stop_temp:
        for i in range(num_iter):
            n = choice([n for n in [v-1,v+1] if 0<=n<99])
            if height[n] > height[v]:
                v = n
            else:
                if exp((height[n]-height[v])/temp) > random():
                    v = n
        print(temp, v, height[v])
        temp *= .99
        canvas.create_rectangle(6*last, (height[last]-mid)*scale+300, 6*last+5, (height[last]-mid)*scale+300+5, fill='white')
        canvas.create_rectangle(6*v, (height[v]-mid)*scale+300, 6*v+5, (height[v]-mid)*scale+300+5, fill='green')
        canvas.update()
        sleep(.1)
        last = v
    return v
        

root = Tk()
canvas = Canvas(width=600, height=600, bg='white')
canvas.grid()

seed(0)

height = [0, 5] + [0]*98
for v in range(2, 100):
    amount = randint(0, 50)
    r = randint(0, 99)
    if height[v-1] - height[v-2] > 0:
        if r < 75:
            height[v] = height[v-1] + amount
        else:
            height[v] = height[v-1] - amount
    else:
        if r < 75:
            height[v] = height[v-1] - amount
        else:
            height[v] = height[v-1] + amount
print(height)

scale = 500/(min(height) - max(height))
mid = (max(height) + min(height)) // 2


for v in range(len(height)-1):
    canvas.create_line(6*v, (height[v]-mid)*scale+300, 6*(v+1), (height[v+1]-mid)*scale+300)

anneal(randint(0, 99))
