# ↓↓

#--------------------------------

# kvadrat ↓↓
# from turtle import*
# color('blue','gray')
# width(5)
# begin_fill()
# for i in range(4):
#     forward(150)
#     left(90)
# end_fill()

# trougao ↓↓
# from turtle import*
# width('5')
# speed(2)
# for i in range(3):
#     forward(150)
#     left(120)
# right(90)
# for i in range(4):
#     forward(150)
#     left(90)

# mala zvezda ↓↓
# from turtle import*
# width(5)
# speed(0)
# for i in range(40):
#     forward(100)
#     backward(100)
#     left(10)
# done()

# DOMACI RAD ↓↓
# from turtle import*
# width('5')
# speed(2)
# for i in range(3):
#     forward(150)
#     left(120)
# right(90)
# for i in range(4):
#     forward(150)
#     left(90)
# forward(150)
# left(90)
# forward(50)
# left(90)
# for i in range(3):
#     forward(50)
#     right(90)
#     forward(20)
#     right(90)

# srednja zvezda ↓↓
# from turtle import*
# width(5)
# color('blue','purple')
# begin_fill()
# for i in range(20):
#     fd(50)
#     bk(50)
#     lt(10)
#     fd(100)
#     bk(100)
#     lt(10)
# end_fill()

# kvadrat u kvadratu ↓↓
# from turtle import*
# width(5)
# for i in range(4):
#     fd(100)
#     lt(90)
# penup()
# lt(45)
# fd(10)
# pendown()
# lt(45)
# for i in range(4):
#     fd(90)
#     rt(90)

# kvadrat unazad ↓↓
# from turtle import*
# width(5)
# lt(20)
# for i in range(20): 
#     fd(100)
#     rt(90)
#     bk(100)
#     rt(90)

# vzba od kuce ↓↓
# from turtle import*
# width(3)
# color('purple','blue')
# fd(60)
# bk(60)
# lt(35)
# begin_fill()
# for i in range(5):
#     fd(100)
#     lt(144)
# end_fill()
# done()

# isprekidani kvadrat ↓↓
# from turtle import*
# shape('turtle')
# color('grey')
# speed(3)
# pensize(4)
# for i in range(4):
#     fd(25)
#     penup()
#     fd(15)
#     pendown()
#     fd(25)
#     penup()
#     fd(15)
#     pendown()
#     fd(25)
#     penup()
#     fd(15)
#     pendown()
#     fd(25)
#     penup()
#     fd(15)
#     pendown()
#     lt(90)
# done()

# kuca,vrata i prozori ↓↓
# from turtle import*
# width(5)
# speed(3)
# ht()
# for i in range(3):
#     forward(150)
#     left(120)
# right(90)
# for i in range(4):
#     forward(150)
#     left(90)
# forward(150)
# left(90)
# forward(50)
# left(90)
# for i in range(2):
#     fd(50)
#     rt(90)
#     fd(20)
#     rt(90)
# fd(50)
# rt(90)
# fd(20)
# pu()
# lt(45)
# fd(30)
# pd()
# rt(45)
# for i in range(4):
#     fd(30)
#     lt(90)
# pu()
# bk(40)
# pd()
# for i in range(4):
#     lt(90)
#     fd(30)
# done()

# srce ↓↓
# from turtle import*
# pensize(5)
# color('black')
# begin_fill()
# fillcolor('red')
# lt(150)
# fd(180)
# circle(-90,180)
# setheading(60)
# circle(-90,180)
# fd(180)
# end_fill()
# ht()
# done()

# velika zvezda ↓↓
# from turtle import*
# width(5)
# speed(3)
# color('red','orange')
# ht()
# begin_fill()
# for i in range(10):
#     fd(200)
#     lt(160)
# end_fill()
# done()

# zgrada ↓↓
# from turtle import*
# color("blue")
# width(5)
# begin_fill()
# forward(100)
# left(90)
# forward(200)
# left(90)
# forward(100)
# left(90)
# forward(200)
# left(90)
# #Vrata
# forward(40)
# left(90)
# forward(30)
# right(90)
# forward(20)
# right(90)
# forward(30)
# #prozori
# left(90)
# forward(40)
# left(90)
# forward(100)
# left(90)
# penup()
# forward(20)
# pendown()
# for i in range(4):
#     forward(20)
#     left(90)
# penup()
# forward(40)
# pendown()
# for i in range(4):
#     forward(20)
#     left(90)
# #drugi sprat
# right(90)
# penup()
# forward(40)
# pendown()
# for i in range(4):
#     forward(20)
#     left(90)
# right(90)
# penup()
# forward(20)
# pendown()
# for i in range(4):
#     forward(20)
#     left(90)
# hideturtle()
# done()

# spirala ↓↓
# from turtle import*
# import colorsys
# bgcolor('black')
# speed(1000)
# pensize(5)
# hue = 0.0
# for i in range(300):
#     color = colorsys.hsv_to_rgb(hue,1,1)
#     pencolor(color)
#     hue +=0.005
#     rt(i)
#     circle(50,i)
#     fd(i)
#     lt(91)
# done()

# sakura cvet ↓↓
# from turtle import*
# import colorsys
# speed(0)
# pensize(2)
# h=0.005
# bgcolor('black')
# for i in range(200):
#     c = colorsys.hsv_to_rgb(h,1,1)
#     color(c)
#     h+=0.004
#     begin_fill()
#     circle(200-i,100)
#     lt(100)
#     circle(200-i,100)
#     for j in range(4):
#         lt(100)
#         rt(20)
#         end_fill()
# done()

#proba ↓↓
# from turtle import*
# import colorsys
# speed(0)
# pensize(2)
# h=0.005
# bgcolor('black')
# for i in range(150):
#     c = colorsys.hsv_to_rgb(h,1,1)
#     color(c)
#     h+=0.004
#     begin_fill()
#     circle(200-i,100)
#     lt(100)
#     circle(200-i,100)
#     for j in range(4):
#         lt(100)
#         rt(20)
#         end_fill()
# done()

# oktagon od oktagona ↓↓
# from turtle import*
# speed(5)
# ht()
# bgcolor('black')
# color('greenyellow')
# pensize(5)
# for i in range(8):
#     lt(45)
#     for i in range(8):
#         fd(100)
#         lt(45)
# done()

# trougao od trouglova ↓↓
# from turtle import*
# pensize(5)
# bgcolor('black')
# color('greenyellow')
# speed(5)
# for i in range(6):
#     lt(60)
#     fd(100)
# for i in range(3):
#     lt(120)
#     fd(200)
#     lt(120)
#     fd(100)
# done()

# devetougao od devetouglova ↓↓
# from turtle import*
# width(5)
# bgcolor('black')
# speed(5)
# color('dark blue')
# for i in range(9):
#     lt(40)
#     for i in range(9):
#         fd(100)
#         lt(40)
# done()

# desetougao od desetouglova ↓↓
# import codecs
# from turtle import*
# import colorsys
# bgcolor('black')
# width(5)
# pencolor('greenyellow')
# speed(5)
# ht()
# for i in range(10):
#     lt(36)
#     for i in range(10):
#         fd(100)
#         lt(36)
# done()

# sareni cvet ↓↓
# from turtle import*
# import colorsys as cs
# setup(800,000)
# speed(0)
# width(2)
# tracer(10)
# bgcolor('black')
# for j in range(25):
#     for i in range(15):
#         color(cs.hsv_to_rgb(i/15,j/25,1))
#         rt(90)
#         circle(200-j*4,90)
#         lt(90)
#         circle(200-j*4,90)
#         rt(100)
#         circle(50,24)
# ht()
# done()

#  cetrnaestougao od cetrnaestouglova ↓↓
# from turtle import*
# width(5)
# bgcolor('black')
# pencolor('greenyellow')
# speed(0)
# for i in range(14):
#     lt(25.71)
#     for i in range(14):
#         fd(50)
#         lt(25.71)
# pencolor('light green')
# for i in range(14):
#     lt(25.71)
#     for i in range(14):
#         fd(70)
#         lt(25.71)
# pencolor('greenyellow')
# for i in range(14):
#     lt(25.71)
#     for i in range(14):
#         fd(50)
#         lt(25.71)
# done()

# kvadrat od kvadrata ↓↓
# from turtle import*
# width(5)
# bgcolor('black')
# pencolor('violet')
# speed(3)
# for i in range(4):
#     lt(90)
#     for i in range(4):
#         fd(100)
#         lt(90)
# pencolor('purple')
# for i in range(4):
#     lt(90)
#     for i in range(4):
#         fd(150)
#         lt(90)
# ht()
# done()

# petougao od petougla ↓↓
# from turtle import*
# width(5)
# speed(3)
# bgcolor('black')
# pencolor('cyan')
# for i in range(5):
#     lt(72)
#     for i in range(5):
#         fd(100)
#         lt(72)
# ht()
# done()


# sarene spirale ↓↓
# import turtle
# wn=turtle.Screen()
# turtle.bgcolor('black')
# turtle.shape('turtle')
# tr=turtle.Turtle()
# ts=turtle.Turtle()
# tt=turtle.Turtle()
# t2=turtle.Turtle()
# t3=turtle.Turtle()
# t4=turtle.Turtle()
# t5=turtle.Turtle()
# move=1
# ###############################
# t5.speed("fastest")
# for i in range(10):
#     for i in range(4):
#           t5.pu()
#           t5.goto(500,200)
#           t5.pd()
#           t5.color('cyan')
#           t5.pensize(3)
#           t5.circle(50,steps=4)
#           t5.right(100)
# t5.speed("fastest")
# for i in range(6):
#     for i in range(4):
#           t5.pu()
#           t5.goto(0,0)
#           t5.pd()
#           t5.color('light green')
#           t5.pensize(3)
#           t5.circle(100,steps=6)
#           t5.right(100)
#           t2.speed("fastest")
# for i in range (10):
#     for i in range (2):
#         t2.pensize(5)
#         t2.goto(270,0)
#         t2.color("green")
#         t2.forward(100)
#         t2.right(60)
#         t2.color("cyan")
#         t2.forward(50)
#         t2.right(120)
#     t2.right(30)
# tr.speed("fastest")
# for i in range (10):
#     for i in range (2):
#         tr.pensize(7)
#         tr.goto(-270,0)
#         tr.color("purple")
#         tr.forward(100)
#         tr.circle(5,steps=4)
#         tr.right(60)
#         tr.color("violet")
#         tr.forward(50)
#         tr.right(120)
#     tr.right(30)
# ts.speed("fastest")
# t5.speed("fastest")
# for i in range(10):
#     for i in range(4):
#           t5.pu()
#           t5.goto(-500,200)
#           t5.pd()
#           t5.color('yellow')
#           t5.pensize(3)
#           t5.circle(50,steps=4)
#           t5.right(100)
# t5.speed("fastest")
# for i in range(10):
#     for i in range(4):
#           t5.pu()
#           t5.goto(-500,-200)
#           t5.pd()
#           t5.color('white')
#           t5.pensize(3)
#           t5.circle(50,steps=3)
#           t5.right(100)
# t5.speed("normal")
# for i in range(10):
#     for i in range(4):
#           t5.pu()
#           t5.goto(500,-200)
#           t5.pd()
#           t5.color('pink')
#           t5.pensize(3)
#           t5.circle(50,steps=3)
#           t5.right(100)
# for i in range (20):
#     for i in range (2):
#         ts.pensize(2)
#         ts.goto(0,300)
#         ts.color("red")
#         ts.forward(100)
#         ts.circle(6,steps=3)
#         ts.right(70)
#         ts.color("yellow")
#         ts.forward(50)
#         ts.right(120)
#     ts.left(30)
# ts.speed('fastest')
# for i in range (20):
#     for i in range (2):
#         ts.pensize(2)
#         ts.pu()
#         ts.goto(0,-300)
#         ts.color("pink")
#         ts.pd()
#         ts.forward(100)
#         ts.circle(6,steps=3)
#         ts.right(70)
#         ts.color("orange")
#         ts.forward(50)
#         ts.right(120)
#     ts.left(30)
# t3.speed("fastest")
# for i in range (10):
#     for i in range (2):
#         t3.pensize(3)
#         t3.goto(-320,300)
#         t3.color("light green")
#         t3.begin_fill()
#         t3.forward(30)
#         t3.right(50)
#         t3.color("green")
#         t3.forward(50)
#         t3.circle(5,steps=6)
#         t3.right(120)
#         t3.end_fill()
#     t3.right(60)
# t3.speed("fastest")
# for i in range (10):
#     for i in range (2):
#         t3.pensize(3)
#         t3.pu()
#         t3.goto(320,-300)
#         t3.pd()
#         t3.color("red")
#         t3.begin_fill()
#         t3.forward(30)
#         t3.right(50)
#         t3.color("orange")
#         t3.forward(50)
#         t3.circle(5,steps=6)
#         t3.right(120)
#         t3.end_fill()
#     t3.right(100)
# t3.speed("fastest")
# for i in range (10):
#     for i in range (2):
#         t3.pensize(3)
#         t3.pu()
#         t3.goto(320,300)
#         t3.pd()
#         t3.color("light blue")
#         t3.begin_fill()
#         t3.forward(30)
#         t3.right(50)
#         t3.color("blue")
#         t3.forward(50)
#         t3.circle(5,steps=6)
#         t3.right(120)
#         t3.end_fill()
#     t3.right(60)
# t3.speed("fastest")
# for i in range (10):
#     for i in range (2):
#         t3.pensize(3)
#         t3.pu()
#         t3.goto(-320,-300)
#         t3.pd()
#         t3.color("orange")
#         t3.begin_fill()
#         t3.forward(30)
#         t3.right(50)
#         t3.color("red")
#         t3.forward(50)
#         t3.circle(5,steps=6)
#         t3.right(120)
#         t3.end_fill()
#     t3.right(60)
# ###########################
# t5.speed("fastest")
# for i in range(10):
#     for i in range(4):
#           t5.pu()
#           t5.goto(600,0)
#           t5.pd()
#           t5.color('white')
#           t5.pensize(1)
#           t5.circle(40,steps=5)
#           t5.right(100)
# t5.speed("fastest")
# ############################
# t5.speed("fastest")
# for i in range(10):
#     for i in range(4):
#           t5.pu()
#           t5.goto(600,0)
#           t5.pd()
#           t5.color('green')
#           t5.pensize(1)
#           t5.circle(20,steps=9)
#           t5.right(100)
# t5.speed("fastest")
# painter = turtle.Turtle()
# painter.pencolor("red")
# for i in range(50):
#     painter.pu()
#     painter.goto(-600,0)
#     painter.pd()
#     painter.forward(100)
#     painter.left(123)
# turtle.done()

# funkcije 
# from turtle import*
# def draw_square():
#     for i in range(0,4):
#         fd(50)
#         lt(90)
#     fd(75)
# def draw_triangle():
#     for i in range(0,3):
#         fd(50)
#         lt(120)
#     fd(75)
# goto(-200,0)
# draw_square()
# draw_triangle()
# draw_square()
# draw_triangle()
# done()

# zvezda ↓↓
# from turtle import*
# width(5)
# speed(2)
# bgcolor('black')
# pencolor('greenyellow')
# for i in range(5):
#     fd(150)
#     lt(144)
# done()

# krug ↓↓
# from turtle import*
# width(5)
# circle(100)

# sunce ↓↓
# from turtle import*
# width(5)
# color('yellow')
# begin_fill()
# circle(100)
# end_fill()
# lt(90)
# fd(85)
# # for i in range(14):
# while True:
#     fd(100)
#     bk(100)
#     lt(25)
# done()

# cvet ↓↓
# from turtle import*
# width(5)
# speed(2)
# pencolor('green')
# rt(90)
# fd(150)
# bk(150)
# lt(90)
# circle(50)
# rt(45)
# pencolor('pink')
# for i in range(5):
#     fd(100)
#     circle(50,180)
#     lt(180)