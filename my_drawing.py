from shapes import  *

paper =Paper()

rect1 = Rectangle()
#To set the attributes of the rectangle object, you can use some special methods called setters.

rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("pink")
rect1.draw()

rect2 = Rectangle()
rect2.set_width(100)
rect2.set_height(50)
rect2.set_color("yellow")

rect2.draw()

paper.display()