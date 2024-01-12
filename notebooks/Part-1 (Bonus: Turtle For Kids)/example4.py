import turtle

gordon = turtle.Pen()
gordon.shape("turtle")

i = 0
while i < 4:
    gordon.forward(100)
    gordon.left(90)
    i = i + 1

turtle.mainloop()
