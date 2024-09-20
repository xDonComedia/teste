import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
cafe1 = "#6D4C41"
cafe2 = "#5D4037"
cafe3 = "#4E342E"
cafe4 = "#3E2723"
verde1 = "#00FF00"
verde2 = "#229954"
verde3 = "#006600"
branco = "#ffffff"
amarelo1 = "#FFEB3B"
amarelo2 = "#FFCA28"
amarelo3 = "#FFA000"
vermelho1 = "#4B0081"
vermelho2 = "#9032BB"
vermelho3 = "#AF69CD"

def quadrado(color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.seth(0)
    t.forward(30)
    t.seth(90)
    t.forward(30)
    t.seth(180)
    t.forward(30)
    t.seth(270)
    t.forward(30)
    t.end_fill()

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def vaso(x, y):
    go(x, y)
    quadrado(cafe1)
    go(x+30, y)
    quadrado(cafe2)
    go(x+60, y)
    quadrado(cafe3)
    go(x+90, y)
    quadrado(cafe3)
    go(x+120, y)
    quadrado(cafe3)
    go(x+150, y)
    quadrado(cafe4)

    go(x, y+30)
    quadrado(cafe1)
    go(x+30, y+30)
    quadrado(cafe1)
    go(x+60, y+30)
    quadrado(cafe2)
    go(x+90, y+30)
    quadrado(cafe1)
    go(x+120, y+30)
    quadrado(cafe3)
    go(x+150, y+30)
    quadrado(cafe4)

    go(x, y+60)
    quadrado(cafe1)
    go(x+30, y+60)
    quadrado(cafe1)
    go(x+60, y+60)
    quadrado(cafe1)
    go(x+90, y+60)
    quadrado(cafe2)
    go(x+120, y+60)
    quadrado(cafe3)
    go(x+150, y+60)
    quadrado(cafe4)

    go(x,y+90)
    quadrado(cafe1)
    go(x+30,y+90)
    quadrado(cafe1)
    go(x+60,y+90)
    quadrado(cafe2)
    go(x+90,y+90)
    quadrado(cafe3)
    go(x+120,y+90)
    quadrado(cafe2)
    go(x+150,y+90)
    quadrado(cafe4)

    go(x,y+120)
    quadrado(cafe1)
    go(x+30,y+120)
    quadrado(cafe2)
    go(x+60,y+120)
    quadrado(cafe1)
    go(x+90,y+120)
    quadrado(cafe1)
    go(x+120,y+120)
    quadrado(cafe3)
    go(x+150,y+120)
    quadrado(cafe2)

    go(x,y+150)
    quadrado(cafe1)
    go(x+30,y+150)
    quadrado(cafe1)
    go(x+60,y+150)
    quadrado(cafe1)
    go(x+90,y+150)
    quadrado(cafe2)
    go(x+120,y+150)
    quadrado(cafe1)
    go(x+150,y+150)
    quadrado(cafe2)

vaso( -210, -300)

go(-150,-120)
quadrado(verde1)
go(-150,-90)
quadrado(verde1)
go(-120,-90)
quadrado(verde2)
go(-120,-60)
quadrado(verde1)
go(-120,-60)
quadrado(verde2)
go(-180,-30)
quadrado(verde2)
go(-150,-30)
quadrado(verde1)
go(-120,-30)
quadrado(verde2)
go(-90,-30)
quadrado(verde2)
go(-210,0)
quadrado(verde2)
go(-180,0)
quadrado(verde1)
go(-150,0)
quadrado(verde1)
go(-150,30)
quadrado(verde1)
go(-150,60)
quadrado(verde1)
go(-120,60)
quadrado(verde2)

go(-180,90)
quadrado(branco)
go(-150,90)
quadrado(branco)
go(-120,90)
quadrado(branco)
go(-210,120)
quadrado(branco)
go(-180,120)
quadrado(branco)
go(-150,120)
quadrado(branco)
go(-120,120)
quadrado(branco)
go(-90,120)
quadrado(branco)
go(-240,150)
quadrado(branco)
go(-210,150)
quadrado(branco)
go(-180,150)
quadrado(amarelo2)
go(-150,150)
quadrado(amarelo1)
go(-120,150)
quadrado(amarelo3)
go(-90,150)
quadrado(branco)
go(-60,150)
quadrado(branco)
go(-240,180)
quadrado(branco)
go(-210,180)
quadrado(branco)
go(-180,180)
quadrado(amarelo1)
go(-150,180)
quadrado(amarelo1)
go(-120,180)
quadrado(amarelo2)
go(-90,180)
quadrado(branco)
go(-60,180)
quadrado(branco)
go(-240,210)
quadrado(branco)
go(-210,210)
quadrado(branco)
go(-180,210)
quadrado(amarelo2)
go(-150,210)
quadrado(amarelo2)
go(-120,210)
quadrado(amarelo1)
go(-90,210)
quadrado(branco)
go(-60,210)
quadrado(branco)
go(-210,240)
quadrado(branco)
go(-180,240)
quadrado(branco)
go(-150,240)
quadrado(branco)
go(-120,240)
quadrado(branco)
go(-90,240)
quadrado(branco)
go(-180,270)
quadrado(branco)
go(-150,270)
quadrado(branco)
go(-120,270)
quadrado(branco)

vaso(90,-300)

go(150,-120)
quadrado(verde3)
go(180,-120)
quadrado(verde3)
go(90,-90)
quadrado(verde3)
go(120,-90)
quadrado(verde3)
go(150,-90)
quadrado(verde3)
go(180,-90)
quadrado(verde3)
go(60,-60)
quadrado(verde3)
go(90,-60)
quadrado(verde3)
go(150,-60)
quadrado(verde1)
go(180,-60)
quadrado(verde3)
go(210,-60)
quadrado(verde3)
go(240,-60)
quadrado(verde3)
go(150,-30)
quadrado(verde1)
go(150,0)
quadrado(verde1)
go(150,30)
quadrado(verde1)
go(90,60)
quadrado(vermelho1)
go(120,60)
quadrado(verde3)
go(150,60)
quadrado(verde3)
go(60,90)
quadrado(vermelho1)
go(90,90)
quadrado(vermelho1)
go(120,90)
quadrado(vermelho1)
go(150,90)
quadrado(vermelho1)
go(180,90)
quadrado(vermelho3)
go(60,120)
quadrado(vermelho1)
go(90,120)
quadrado(vermelho2)
go(120,120)
quadrado(vermelho3)
go(150,120)
quadrado(vermelho2)
go(180,120)
quadrado(vermelho1)
go(210,120)
quadrado(vermelho3)
go(90,150)
quadrado(vermelho1)
go(120,150)
quadrado(vermelho2)
go(150,150)
quadrado(vermelho3)
go(180,150)
quadrado(vermelho1)
go(210,150)
quadrado(vermelho2)
go(150,180)
quadrado(vermelho3)
go(180,180)
quadrado(vermelho3)

t.hideturtle()
turtle.done()