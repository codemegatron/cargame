import sys, pygame
from pygame.locals import *

pygame.init()
bg = pygame.image.load("PygameSimplifiedVersionII/images/track2.png")

screen = pygame.display.set_mode((400,550))
black = 0, 0, 0
car = pygame.image.load("PygameSimplifiedVersionII/images/car.png")

carrect = car.get_rect()
print("x: {}, y:{}, w:{}, h:{}".format(carrect.x, carrect.y, carrect.width, carrect.height))

class Vehicle:
	speed = 0
	angle = 0
	x = 0
	y = 0
	
	def accelerate(self):
		self.speed += 5
	def deccelerate(self):
		self.speed -= 5
	def turnLeft(self):
		self.angle += 10
	def turnRight(self):
		self.angle -= 10
		
		
playerCar = Vehicle()


	
while True:
	
	key = pygame.key.get_pressed()
	dist = 1
	if key[pygame.K_LEFT]:
		playerCar.turnLeft()
		#car = pygame.transform.rotate(car,10)
	if key[pygame.K_RIGHT]:
		playerCar.turnRight()
		#car = pygame.transform.rotate(car,-10)
	if key[pygame.K_UP]:
		playerCar.accelerate()
		#carrect.move_ip(0, -1)
	if key[pygame.K_DOWN]:
		playerCar.deccelerate()
		#carrect.move_ip(0, 1)
	
	pygame.event.get()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			break
	screen.fill(black)
	screen.blit(car, carrect)
	pygame.display.flip()
	pygame.display.update()
	
