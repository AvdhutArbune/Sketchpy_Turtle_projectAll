from turtle import *
speed(0.5)
hideturtle()
bgcolor("black")
for i in range(175):
    color("green")
    circle(i)
    color("white")
    circle(i*1.2)
    color("red")
    circle(i*1.5)
    left(5)
    backward(5)
    
done()    
   

        