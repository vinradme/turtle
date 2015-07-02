import turtle

turtle.penup()
colors = ['pink', 'red', 'green']
nums = [150, 100, 50]

for cir_color, num in zip(colors, nums): 
    turtle.begin_fill()
    turtle.color(cir_color)
    turtle.right(90)    # Face South
    turtle.forward(num)   # Move one radius
    turtle.right(270)   # Back to start heading
    turtle.pendown()    # Put the pen back down
    turtle.circle(num)    # Draw a circle
    turtle.penup()      # Pen up while we go home
    turtle.home()       # Head back to the start pos
    turtle.end_fill()
