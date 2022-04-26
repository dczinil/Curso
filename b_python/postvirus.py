from turtle import*
title("Covid")
setup(1100, 700, 0, 0)
showturtle()
speed (40)
color ("cyan")
bgcolor("black")
b = 200
while b > 0:
    position()
    left(b)
    forward( b*3)
    b = b-1
end_fill()
done()




