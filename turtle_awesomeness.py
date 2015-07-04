# turtle_awesomeness.py
import turtle

x = 10
while x:
    turtle.forward(x)
    turtle.left(120)
    x = x + 5
    
    if x == 95:
        choice = raw_input("Press enter to terminate: ")
        if choice == "enter":
            break
        else:
            continue
