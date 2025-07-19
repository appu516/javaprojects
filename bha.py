import turtle
def draw_multicolor_square(animal,size):
    for color in ["red","purple","hotpink","blue"]:
        animal.color(color)
        animal.forward(size)
        animal.left(90)
        
    window=turtle.screen()
    window.bgcolor("lightgreen")
    
    tess=turtle.Turtle()
    tess.pensize(3)
    
    size=20
    for i in range(15):
        draw_multicolor_square(tess,size)
        size +10
        tess.forward(10)
        tess.right(18)
        window.mainloop()
