import pygame
from math import *
from random import randint

# some variables

_x = 200
_y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (_x,_y)

width = 1050
height = 600
par = 1

#--------- colors ------------------------------------------#
black = (0,0,0)
white = (255,255,255)
yellow = (220,220,20)
red = (255,0,0)

#-------- functions ----------------------------------------#
def drawGraph(screen, yHeight, function, deltaX, time, txt):
    pygame.draw.line(screen, white, (0,yHeight),(width,yHeight))
    n = int(width/deltaX)
    for i in range(n):
        pygame.draw.circle(screen, red, (int(deltaX*i), int(yHeight+function(deltaX*i,time))), 1, 1)
    font = pygame.font.SysFont("Liberation Serif", 20)
    text = font.render(txt, True, white)
    screen.blit(text,(20,yHeight-50))
                
def f1(x,t):
    # Here I actually did things a little different, I plotted a
    # function on both space and time, basically the
    # space-time wave function is Acos(kx-wt) where
    # k is the wave number (k=2pi/lambda) (and lambda is the wavelength),
    # and w is the angular frequency (w = 2pi*frequency).
    # We then know that wavelength (aka lambda) and
    # the frequency are related since sound moves with a definite
    # velocity: v = lambda*frequency, therefore
    # with some math: lambda = 2pi/k, frequency = w/2pi
    # and we obtain v = k/w

    # you can modify these three parameters
    v = 3000
    f1 = 150
    f2 = 160
    # we find the w
    w1 = 2*pi*f1
    w2 = 2*pi*f2
    # we find the k
    # and for that we firstly find lambda
    l1 = v/f1
    l2 = v/f2
    k1 = 2*pi/l1
    k2 = 2*pi/l2
    # par is a zoom factor, you can zoom using w or s
    x *= par

    #---------------------------------------------------
    # In the video I actually used a different formula
    # I leave it commented if u want to use it.
    # Honestly speaking that wave is impossible to
    # produce in the world since I came up with the
    # coefficients just by tuning them randomly and
    # they don't respect the v=lambda*frequency equation
    # with the velocity of sound being constant, but
    # the animation they produce is pretty cool
    #return 50*sin(x/120-t*35)*sin(x/3-t*35)
    #---------------------------------------------------
    return 25*cos(k1*x-w1*t)+25*cos(k2*x-w2*t)


def updateGame(screen, time):
    drawGraph(screen, 300, f1, 0.1, time, "Wave1")
    font = pygame.font.SysFont("Liberation Serif", 20)
    text = font.render("Resolution: x"+str(1/par), True, white)
    screen.blit(text,(width-350,height-30))

#----------- main -------------------------------------------#
pygame.init()

screen = pygame.display.set_mode( (width, height) )
fpsClock = pygame.time.Clock()

running = True

time = 0
deltaT = 0.001

while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                par *= 1.5
            if event.key == pygame.K_s:
                par /= 1.5

    updateGame(screen, time)
    pygame.display.update()
    time += deltaT
    fpsClock.tick(90)

pygame.quit()
