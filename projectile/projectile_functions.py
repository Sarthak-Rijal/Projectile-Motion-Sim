import math
import pygame
pygame.init()


def projectile(x_pos,y_pos, power, angle,HEIGHT,time):

    x_pos_final = int(x_pos + power*math.cos(math.radians(angle)) * time)
    y_pos_final = int(-1*(y_pos + power*math.sin(math.radians(angle))*time + .5*(-10)*time**2)+HEIGHT)
    return x_pos_final, y_pos_final        

def print_f(msg,siz,color,x,y):
    Text = pygame.font.Font("freesansbold.ttf",siz)
    write = Text.render(msg,True,color)
    write_rect = write.get_rect()
    write_rect.center = ((x),(y))
    screen.blit(write,write_rect)

def touches_boundry(siz,x,y,WIDTH,HEIGHT):
    if x+radius > WIDTH:
        return True
    if y+radius > HEIGHT:
        return True

