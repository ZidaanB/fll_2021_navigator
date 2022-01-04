import turtle

llcords = (-200, -200)
currentPos = llcords
num_rows = 4
num_cols = 3
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
currentPos = t.pos()
t.penup()
t.goto(llcords[0] + (num_rows*aisle_side_len),llcords[1] + (aisle_side_len*num_cols))
turtle.Screen().exitonclick()
