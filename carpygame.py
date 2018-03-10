import sys, pygame
from pygame.locals import *

pygame.init()
bg = pygame.image.load("PygameSimplifiedVersionII/images/track2.png")

screen = pygame.display.set_mode((400,550))
black = 0, 0, 0
car = pygame.image.load("PygameSimplifiedVersionII/images/car.png")

carrect = car.get_rect()
print("x: {}, y:{}, w:{}, h:{}".format(carrect.x, carrect.y, carrect.width, carrect.height))
	
while True:
	
	key = pygame.key.get_pressed()
	dist = 1
	if key[pygame.K_LEFT]:
		car = pygame.transform.rotate(car,10)
	if key[pygame.K_RIGHT]:
		car = pygame.transform.rotate(car,-10)
	if key[pygame.K_UP]:
		carrect.move_ip(0, -1)
	if key[pygame.K_DOWN]:
		carrect.move_ip(0, 1)

	
	pygame.event.get()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			break
	screen.fill(black)
	screen.blit(car, carrect)
	pygame.display.flip()
	pygame.display.update()
	
