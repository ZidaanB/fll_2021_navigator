import turtle
import string

llcords = (-200, -300)
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
t.goto(llcords[0], currentPos[1])
currentPos = t.pos()
t.penup()


def drawColumnLine(x, y, endx, endy):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(endx, endy)


def drawRowLine(x, y, endx, endy):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(endx, endy)


for i in range(1, num_rows):
    drawColumnLine(llcords[0] + (aisle_side_len * i), llcords[1] + (aisle_side_len * num_cols),
                   llcords[0] + (aisle_side_len * i), llcords[1])
for i in range(1, num_cols):
    drawColumnLine(llcords[0], llcords[1] + (i * aisle_side_len), llcords[0] + (aisle_side_len * num_rows),
                   llcords[1] + (i * aisle_side_len))


# Draw text onto the aisle grid
def drawText(text, x, y):
    t.penup()
    t.goto(x, y)
    t.write(text, move=False, font=(('Arial', 16, 'normal')))


for j in range(0, num_cols):
    alphabets = string.ascii_uppercase
    for i in range(0, num_rows):
        drawText(f"{alphabets[i]}{j+1}", (i * aisle_side_len) + llcords[0] + (aisle_side_len / 2),
                 llcords[1] + ((num_cols * aisle_side_len) - (aisle_side_len / 2) - (j * aisle_side_len)))
turtle.Screen().exitonclick()
