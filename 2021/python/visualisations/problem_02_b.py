# NMB
# Advent of Code 2021
# Problem 02b

import turtle, time

win = turtle.Screen()
win.title("Advent of Code 2021 - Problem 2b")
win.bgcolor("black")
WIDTH, HEIGHT = 1200, 700
win.setup(width=WIDTH, height=HEIGHT)
win.tracer(0)
delay = 0.01

lines = open('~/../../input_2.txt','r').read().splitlines()
h, d, a = 0, 0, 0

colour_1 = (36/255, 211/255, 255/255)
colour_2 = (31/255, 43/255, 220/255)

deltas = [(hue - colour_1[i]) / HEIGHT for i, hue in enumerate(colour_2)]

gradient = turtle.Turtle()
gradient.color(colour_1)
gradient.penup()
gradient.goto(-WIDTH/2, 250)
gradient.pendown()
direction = 1
for distance, y in enumerate(range(250, -HEIGHT//2, -1)):
    gradient.forward(WIDTH * direction)
    gradient.color([colour_1[i] + delta * distance for i, delta in enumerate(deltas)])
    gradient.sety(y)
    direction *= -1

sub = turtle.Turtle()
win.addshape("./Visualisations/images/sub.gif")
sub.shape('./Visualisations/images/sub.gif')
sub.color('white')
sub.penup()
sub.goto(-500,250)
sub.pendown()
sub.speed(0)

text = turtle.Turtle()
text.color('white')
text.penup()
text.setx(-500)
text.sety(290)
text.hideturtle()
text.write(str(h)+' '+str(d)+' '+str(a))

for line in lines:
    text.clear()
    text.write('hor: '+str(h)+'  dep: '+str(d)+'  aim: '+str(a))        
    tokens = line.split(" ")
    if tokens[0] == "forward":
        h += int(tokens[1])
        d += a*int(tokens[1])
    elif tokens[0] == "down":
        a += int(tokens[1])
    else:
        a -= int(tokens[1])
    sub.setx(-500+h/2)
    sub.sety(250-d/2000)
    win.update()
    time.sleep(delay)
    
print(d*h)
