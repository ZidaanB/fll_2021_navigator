import turtle

llcords = (-200, -200)
currentPos = llcords
num_rows = 6
num_cols = 6
aisle_side_len = 100
# Draw the basic screen
screen = turtle.getscreen()
t = turtle.Turtle()

# Draw the aisle grid
t.penup()
t.goto(llcords)
t.pendown()
t.goto(currentPos[0], currentPos[1] + (num_cols * aisle_side_len))
currentPos = t.pos()
t.goto(currentPos[0] + (num_rows * aisle_side_len), currentPos[1])
currentPos = t.pos()
t.goto(currentPos[0], currentPos[1] - (num_cols * aisle_side_len))
currentPos = t.pos()
t.goto(llcords[0],currentPos[1])
turtle.Screen().exitonclick()
