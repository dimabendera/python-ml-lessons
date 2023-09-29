import turtle

gordon = turtle.Pen()

gordon.shape("turtle")
gordon.color("blue")
gordon.width(3)
i = 0
while i < 20:
    gordon.forward(10*i)
    gordon.left(90)
    i += 1


turtle.mainloop()
