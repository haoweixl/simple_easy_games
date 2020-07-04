import turtle as t


#位移函数
def Skip(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#画笔基础设置
t.screensize(1200,800)
t.pensize(5)#设置笔宽
t.hideturtle()
t.speed(20)
t.pencolor("red")#设置笔的颜色

#画笔移动


#画房盖
Skip(-200,100)
t.begin_fill()
t.pencolor("gold")
t.fillcolor("gold")
t.circle(40,90)
t.right(90)
t.forward(200)
t.right(90)
t.circle(40,90)
t.right(180)
t.forward(280)
t.end_fill()

#顶层
#print(t.pos())
Skip(-200,100)
t.pencolor("black")
t.left(135)
t.forward(20)
t.left(45)
t.forward(252)
t.left(45)
t.forward(20)


Skip(-184,82)
t.right(135)
t.forward(20)
t.left(90)
t.forward(249)
t.left(90)
t.forward(20)

#第二层屋檐
Skip(-184,62)
t.begin_fill()
t.pencolor("gold")
t.fillcolor("gold")
t.left(110)
t.forward(50)
t.circle(-40,50)
t.left(150)
t.circle(30,60)
t.forward(354)
t.circle(30,60)
t.left(150)
t.circle(-40,50)
t.forward(50)
t.end_fill()


#第二层
Skip(-214,30)
t.pencolor("red")
t.left(110)
t.forward(30)
t.left(90)
t.forward(309)
t.left(90)
t.forward(30)

#第二层柱子
t.left(180)
Skip(-183,30)
t.forward(25)
Skip(-152,30)
t.forward(25)
Skip(-121,30)
t.forward(25)
Skip(-90,30)
t.forward(25)
Skip(-59,30)
t.forward(25)
Skip(-28,30)
t.forward(25)
Skip(3,30)
t.forward(25)
Skip(34,30)
t.forward(25)
Skip(65,30)
t.forward(25)
t.left(180)





# 旗帜
Skip(270,8)
t.pensize(2)
t.pencolor("black")
t.forward(50)
Skip(270,58)
t.begin_fill()
t.pencolor("red")
t.fillcolor("red")
t.right(90)
t.forward(22)
t.right(90)
t.forward(16)
t.right(90)
t.forward(22)
t.end_fill()
t.right(90)

Skip(225,8)
t.pensize(2)
t.pencolor("black")
t.forward(50)
Skip(225,58)
t.begin_fill()
t.pencolor("red")
t.fillcolor("red")
t.right(90)
t.forward(22)
t.right(90)
t.forward(16)
t.right(90)
t.forward(22)
t.end_fill()
t.right(90)

Skip(-340,8)
t.pensize(2)
t.pencolor("black")
t.forward(50)
Skip(-340,58)
t.begin_fill()
t.pencolor("red")
t.fillcolor("red")
t.right(90)
t.forward(22)
t.right(90)
t.forward(16)
t.right(90)
t.forward(22)
t.end_fill()
t.right(90)


Skip(-395,8)
t.pensize(2)
t.pencolor("black")
t.forward(50)
Skip(-395,58)
t.begin_fill()
t.pencolor("red")
t.fillcolor("red")
t.right(90)
t.forward(22)
t.right(90)
t.forward(16)
t.right(90)
t.forward(22)
t.end_fill()
t.right(90)


#外墙
Skip(-214,3)
t.begin_fill()
t.pencolor("darksalmon")
t.fillcolor("darksalmon")
t.left(90)
t.forward(250)
t.left(90)
t.forward(100)
t.left(90)
t.forward(809)
t.left(90)
t.forward(100)
t.left(90)
t.forward(250)
t.end_fill()

Skip(-464,-15)
t.left(180)
t.forward(383)

Skip(-37,-15)
t.forward(383)

#正门和侧门
Skip(-79,-97)
t.begin_fill()
t.pencolor("brown")
t.fillcolor("brown")
t.left(90)
t.forward(15)
t.circle(-20,180)
t.forward(15)
t.end_fill()


Skip(-189,-97)
t.begin_fill()
t.pencolor("brown")
t.fillcolor("brown")
t.left(180)
t.forward(10)
t.circle(-15,180)
t.forward(10)
t.end_fill()


Skip(31,-97)
t.begin_fill()
t.pencolor("brown")
t.fillcolor("brown")
t.left(180)
t.forward(10)
t.circle(-15,180)
t.forward(10)
t.end_fill()

Skip(-269,-97)
t.begin_fill()
t.pencolor("brown")
t.fillcolor("brown")
t.left(180)
t.forward(10)
t.circle(-15,180)
t.forward(10)
t.end_fill()

Skip(111,-97)
t.begin_fill()
t.pencolor("brown")
t.fillcolor("brown")
t.left(180)
t.forward(10)
t.circle(-15,180)
t.forward(10)
t.end_fill()

#文字
Skip(-340,-15)
t.begin_fill()
t.pencolor("red")
t.fillcolor("red")
t.forward(20)
t.left(90)
t.forward(180)
t.left(90)
t.forward(20)
t.end_fill()
Skip(-335,-35)
t.pencolor("snow")
t.write("中华人民共和国万岁", font = ("Times", 12 ))


Skip(25,-15)
t.begin_fill()
t.pencolor("red")
t.fillcolor("red")
t.left(180)
t.forward(20)

t.left(90)
t.forward(180)
t.left(90)
t.forward(20)
t.end_fill()
Skip(30,-35)
t.pencolor("snow")
t.write("世界人民大团结万岁", font = ("Times", 12 ))

#画框
Skip(-77,-4)
t.pencolor("red")
t.left(180)
t.forward(45)
t.left(90)
t.forward(36)
t.left(90)
t.forward(45)
t.left(90)
t.forward(36)
t.done()
#Skip(-77,44)


# Skip(-420, -97)
# t.pensize(12)
# t.pencolor("black")
# t.forward(80)
# Skip(-415,-97)
# t.forward(80)


# t.begin_fill()
# t.pencolor("red")
# t.fillcolor("red")
# t.right(90)
# t.forward(22)
# t.right(90)
# t.forward(16)
# t.right(90)
# t.forward(22)
# t.end_fill()
# t.right(90)
