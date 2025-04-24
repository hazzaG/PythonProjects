import pygame
import sys

pygame.joystick.init()
#joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
#print(joysticks)
stick = pygame.joystick.Joystick(0)
thrust =  pygame.joystick.Joystick(1)


class Player(object):
    def __init__(self):
        self.player = pygame.rect.Rect((300,400,50,50))
        self.color = "white"

    def move(self, x_speed, y_speed):
        self.player.move_ip((x_speed,y_speed))

    def change_color(self,color):
        self.color = color

    def draw(self, game_screen):
        pygame.draw.rect(game_screen, self.color, self.player)

pygame.init()

player = Player()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
            #print(pygame.joystick.Joystick(0).get_button)
            if stick.get_button(0):
                player.change_color("red")
            if stick.get_button(1):
                player.change_color("cyan")
            if stick.get_button(2):
                player.change_color("orange")
            if stick.get_button(3):
                player.change_color("green")
        #if event.type == pygame.JOYAXISMOTION:
                #print(event)


        x_speed = round(stick.get_axis(0))
        y_speed = round(stick.get_axis(1))
        player.move(x_speed, y_speed)


    screen.fill((0,0,0))
    player.draw(screen)
    pygame.display.update()

    clock.tick(180)