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

oval1 = Oval()
oval1.randomize()
oval1.draw()

tri = Triangle(5, 5, 100, 5, 100, 200)
tri.set_color('purple')
tri.draw()
paper.display()