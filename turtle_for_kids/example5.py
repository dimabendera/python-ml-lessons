import turtle

gordon = turtle.Pen()

gordon.shape("turtle")
gordon.width(3)

i = 0
while i < 4:
    gordon.forward(100)
    gordon.left(90)
    i = i + 1


gordon.up()
gordon.forward(200)
gordon.down()

i = 0
while i < 4:
    gordon.forward(100)
    gordon.left(90)
    i = i + 1

turtle.mainloop()
