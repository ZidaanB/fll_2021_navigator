import turtle
import string
screen = turtle.getscreen()
t = turtle.Turtle()
# Draw out the grid
t.color("red")
StoreWidth = 300
StoreHeight = 300
Offset_Value = StoreHeight/6
GridlinePos = StoreWidth/3
t.goto(0, 0)
t.goto(StoreWidth, 0)
t.goto(StoreWidth, StoreHeight)
t.goto(0, StoreHeight)
t.goto(0, 0)
t.penup()
t.setpos(StoreWidth / 3, StoreHeight / 3)
t.pendown()
t.goto(StoreWidth / 3, 0)
t.showturtle()
t.goto(StoreWidth / 3, StoreHeight)
t.goto(StoreWidth / 1.5, StoreHeight)
t.goto(StoreWidth / 1.5, 0)
t.penup()
t.goto(0, StoreHeight / 3)
t.pendown()
t.goto(StoreWidth, StoreHeight / 3)
t.goto(StoreWidth, StoreHeight / 1.5)
t.goto(0, StoreHeight / 1.5)
t.penup()


# Draw the text separating the aisles
def writeText(xp, yp, row, column):
    t.color('black')
    t.goto(xp, yp)
    t.write(f"{row}{column}", move=False, font=('Arial', 16, 'normal'))


writeText(StoreWidth/6, StoreHeight - ((StoreHeight / 3) / 2), "A", "1")
writeText(StoreWidth/6,StoreHeight/2 ,"A","2")
writeText(StoreWidth/6,StoreHeight/6, "A","3")

writeText(StoreWidth/2, StoreHeight - ((StoreHeight / 3) / 2),"B", "1")
writeText(StoreWidth/2,StoreHeight/2,"B","2")
writeText(StoreWidth/2, StoreWidth/6,"B","3")

writeText(StoreWidth-(StoreWidth/6), StoreHeight - ((StoreHeight / 3) / 2),"C", "1")
writeText(StoreWidth-(StoreWidth/6),StoreHeight/2,"C","2")
writeText(StoreWidth-(StoreWidth/6), StoreWidth/6,"C","3")
# Fill each individual aisle
t.penup()
t.goto(StoreWidth/3,StoreHeight)
t.color('blue')
t.pendown()
t.goto(StoreWidth/3,0)

t.penup()
t.goto(StoreWidth - (StoreWidth/3),StoreHeight)
t.color('yellow')
t.pendown()
t.goto(StoreWidth - (StoreWidth/3),0)

# Make the turtle move along the optimal path
optimal_route = ["A1","A2","B2","C1"]
aisle_point_screen = []
def find_point_on_screen(aisle):
    aisle = str(aisle)
    first_val = aisle[0]
    second_val = int(aisle[1])
    alphabet = string.ascii_uppercase
    cord_list = []
    cord_list.append(alphabet.index(first_val))
    cord_list.append(second_val - 1)
    # Operate on column value (sW/3, sH/6 for centering)
    if cord_list[0] == 0:
        aisle_point_screen.append((GridlinePos)-Offset_Value)
    else:
        aisle_point_screen.append((cord_list[0]*GridlinePos)+Offset_Value)

    # Operate on row value (sW/6 sH/3 for centering)
    if cord_list[1] == 0:
        aisle_point_screen.append((GridlinePos)-Offset_Value)
    else:
        aisle_point_screen.append((cord_list[1]*GridlinePos)+Offset_Value)
    return aisle_point_screen
numAisles_in_route = len(optimal_route)
t.penup()
t.color('black')
print(type(optimal_route[0]))
print(optimal_route[0])
print(find_point_on_screen('A3'))
t.goto(find_point_on_screen("A3")[0], find_point_on_screen("A3")[1])
#t.goto(find_point_on_screen(int(optimal_route[0][0]),)
turtle.Screen().exitonclick()
