from turtle import *



speed(20)
width(7)
color("purple")
forward(200)
left(90)

forward(200)        
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square
# we want to paint a house

#step 1:    draw a square

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)      
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("blue")
begin_fill()
left(30)
forward(65)
left(90)
forward(60)
left(90)
forward(65)
end_fill()


color("blue")
begin_fill()
right(90)
forward(75)
right(90)
forward(65)
left(90)
forward(65)
left(90)    
forward(65)
left(90)
forward(65)
end_fill()

exitonclick()