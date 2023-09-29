import turtle

gordon = turtle.Pen()
gordon.shape("turtle")
gordon.speed(0)

i = 0
while i < 50:
    gordon.circle(i*3)
    gordon.left(10)
    i += 1


turtle.mainloop()
