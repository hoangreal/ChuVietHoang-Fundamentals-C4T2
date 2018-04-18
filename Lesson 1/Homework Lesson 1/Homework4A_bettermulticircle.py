from turtle import *
shape("turtle")
color("green")
speed (-1)
n = int(input("Your number of circle: "))
for i in range(n):
    circle(100)
    right(360/n)
done()
