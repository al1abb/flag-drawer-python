from turtle import Turtle, Screen as TScreen
from colors import Colors
from constants import *

# Create a Turtle Screen object
screen = TScreen()

# Set the window title and background color
screen.title("AZE Flag")
screen.bgcolor("white")

# Create a turtle object
t = Turtle()
t.speed(0)

# Draw rectangle function
def draw_rectangle(color, width=RECT_WIDTH, height=RECT_HEIGHT):
    t.begin_fill()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    
# Draw crescent function
def draw_crescent():
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    t.color(Colors.WHITE.value)
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    
    t.penup()
    t.goto(-143, 104.5)
    t.pendown()
    t.color(Colors.RED.value)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    t.penup()
    t.goto(0, 15)
    t.pendown()
    t.color(Colors.WHITE.value)
    t.begin_fill()
    for _ in range(5):
        t.forward(40)
        t.right(144)
    t.end_fill()

# Draw star function
def draw_star(size):
    t.begin_fill()
    t.penup()
    t.goto(-130, 128)
    t.pendown()
    for _ in range(8):
        t.color(Colors.WHITE.value)
        t.forward(size)
        
		# 360/8 * 2 = 135 degrees to make the star shape
        t.right(135)
    t.end_fill()

# Drawing the flag
t.penup()
t.goto(-300, 150)
t.pendown()

# Drawing blue rectangle
draw_rectangle(Colors.BLUE.value, RECT_WIDTH, RECT_HEIGHT)

t.penup()
t.goto(-300, 100)
t.pendown()

# Drawing red rectangle
draw_rectangle(Colors.RED.value, RECT_WIDTH, RECT_HEIGHT)

t.penup()
t.goto(-300, 50)
t.pendown()

# Drawing green rectangle
draw_rectangle(Colors.GREEN.value, RECT_WIDTH, RECT_HEIGHT)

t.penup()
t.goto(-250, 75)
t.pendown()

# Draw the crescent
draw_crescent()

# Draw the star
draw_star(20)

# Keep the window open until the user closes it
screen.mainloop()