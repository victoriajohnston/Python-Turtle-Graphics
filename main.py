# Ms. Victoria Johnston 3/4/2023
# Introduction to Computer Science
# Python Turtle Graphics Lesson #1
# Baruch College STEP Academy

import turtle
turtle.showturtle()
turtle.shape("turtle")
turtle.forward(100)

# Practice For Loop
for x in range(5):
  print("Hello, world!")

# Draw a triangle
turtle.showturtle()
turtle.shape("turtle")
for x in range(3):
  turtle.forward(50)
  turtle.left(120)

# Draw a square
turtle.showturtle()
turtle.shape("turtle")
for x in range(4):
  turtle.forward(50)
  turtle.right(90)

# Draw a pentagon
turtle.showturtle()
turtle.shape("turtle")
for x in range(5):
  turtle.forward(50)
  turtle.left(72)

# Draw a spiral
turtle.showturtle()
turtle.shape("turtle")
for x in range(100):
  turtle.forward(x)
  turtle.left(91)

# Draw a star
turtle.showturtle()
turtle.shape("turtle")
turtle.pencolor('green')
for x in range(100):
    turtle.forward(200)
    turtle.left(175)