import pygame
#import pydub
from tone import Tone

pygame.init()

pygame.joystick.init()
#joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
#print(joysticks)
stick = pygame.joystick.Joystick(0)
thrust =  pygame.joystick.Joystick(1)

clock = pygame.time.Clock()

def axis_to_tone():  
    while True:
        '''
        '''
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if stick.get_button(6): break
        x_speed = stick.get_axis(0)
        p=0
        p = Tone.sine(((x_speed+1)*1000), p, duration=0.01)
        clock.tick(100)

def hum():
    Tone.sine(10, duration=200)


#hum()
axis_to_tone()



