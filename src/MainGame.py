#File that the main game will run in

#Libraries
import pygame
from sys import *

#global variables
placeholder = pygame.image.load("src/imgs/placeholder.png")

#setup
window = pygame.display.set_mode((800,800))
pygame.display.set_caption("Placeholder")
run = True
#Gameloop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
    pygame.display.update()