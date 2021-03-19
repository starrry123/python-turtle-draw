#https://pythonturtle.academy/fully-connected-24-gon/
#this is my implementation

from turtle import *
screensize(2000,2000)
speed(9)
n=24
L=100
deg=360/n
pencolor('red')
data=[]
for i in range(n):
    data.append(position())
    forward(L)
    left(deg)

for i in range(0,len(data)-2):
    up()
    goto(data[i])
    pos1=position()
    down()
    for j in range(i+2,len(data)):
        goto(data[j])
        goto(pos1)
