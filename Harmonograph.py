from turtle import *
import random as r
import colorsys                
from math import sin, pi
 
colour = False                  
if colour:  bgc = "black"
else:       bgc = "white"
width, height = 752, 382        
npen = 3                        # number of pendulums
dd = 0.9999                     # decay factor
dt = 0.018                      # time increment
sd = 0.008                      # frequency spread (from integer)
mf = 5                          # max range for frequencies
end = 0.25                      # end when decay this low
linewidth = 1                   # line width
hui = dt/(2*pi)                 # hue increment (for colour)
xscale, yscale = width / (npen * 1.8), height / (npen * 1.8)
 
def fuzzint(mf, sd):
#    return r.gauss(r.randint(1, mf), sd) # nit gauss()
    return r.randint(1, mf) + sd  # so just add some small number
 
#   Compute frequencies & phases
fxy = [[fuzzint(mf, sd)     for p in range(npen)] for q in range(2)]
#pxy = [[r.uniform(0, 2*pi)  for p in range(npen)] for q in range(2)]  # nit uniform()
pxy = [[r.randint(0, 7)  for p in range(npen)] for q in range(2)]
 
canvas = Screen()               # Set up Turtle canvas (or window)
canvas.setup(width, height)
canvas.bgcolor(bgc)

tt = Turtle()
tt.width(linewidth)
tt.speed("fastest")
def exit(x, y): canvas.bye()    # exit if canvas is clicked
canvas.onclick(exit)

hue = 0
t = 0.0                         # teha
dec = 1.0                       # daecy factor
first = True                   
tt.penup()
 
while dec > end:               
                                    
    xy = [sum(sin(t * fxy[q][p] + pxy[q][p])    for p in range(npen))
                                                for q in range(2)]
    if colour:  tt.color(colorsys.hsv_to_rgb(hue, 1.0, 1.0))
    tt.goto(xy[0]*xscale*dec, xy[1]*yscale*dec)
    dec *= dd
    hue += hui
    if first:                   
        first = False
        tt.pendown()               
    t += dt                     # increment angle for sine
canvas.exitonclick()
