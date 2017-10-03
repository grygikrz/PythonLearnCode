import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")
    
    brad = turtle.Turtle()
    brad.color("red")
    brad.shape("turtle")
    brad.speed(4)
    
    for i in range(1,57):
        brad.forward(200)
        brad.right(90)
        brad.right(5)

   
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(200)

    window.exitonclick()
    
draw_square()
