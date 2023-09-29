import random
import turtle

gordon = turtle.Pen()
gordon.shape("turtle")
gordon.width(3)
# gordon.speed(0)

i = 0
while i < 100:
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    gordon.up()
    gordon.goto(x, y)
    gordon.down()

    size = random.randrange(10, 200)
    j = 0
    while j < 4:
        gordon.forward(size)
        gordon.left(90)
        j += 1
    i += 1


turtle.mainloop()
