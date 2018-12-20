import turtle

window = turtle.Screen()
window.bgcolor("blue")
wow = turtle.Turtle()
wow.shape("turtle")
wow.color("red")
wow.speed(15)

def draw_square():
     for n in range (1,5):
        wow.forward(100)
        wow.right(90)

for i in range (1,36):
    draw_square()
    wow.right(10)

for i in range (1,36):
    wow.right(25)
    draw_square()
