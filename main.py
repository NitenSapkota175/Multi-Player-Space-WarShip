import pygame
import os

WIDTH , HEIGHT = 900 ,500   # depends on  your screen resolution if you are in a low resolution screen it might take huge chucks of your window  
WIN = pygame.display.set_mode((WIDTH,HEIGHT))  # here there is a tuple in display.set_mode((tuple))

#VELOCITY 
VEL = 5
FPS = 60
# to set the window name 
pygame.display.set_caption("Spaceship war")

#images 
YELLOW_SPACESHIP_IMAGE =  pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
RED_SPACESHIP_IMAGE =  pygame.image.load(os.path.join('Assets','spaceship_red.png'))

# resize spaceships
SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55 , 40
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP =  pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

BOARDER = pygame.Rect(WIDTH / 2 - 5 , 0 , 10 , HEIGHT )
WHITE  = (255,255,255)
BLACK = (0,0,0,0)

def draw_window(yellow,red):
	WIN.fill(WHITE)
	pygame.draw.rect(WIN,BLACK,BOARDER)
	WIN.blit(YELLOW_SPACESHIP,(yellow.x , yellow.y))
	WIN.blit(RED_SPACESHIP,(red.x ,red.y))
	pygame.display.update()

def handle_yellow_movement(keys_pressed , yellow):
		if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #LEFT
			yellow.x -= VEL 
		
		if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
			yellow.y -= VEL 

		if keys_pressed[pygame.K_d] and yellow.x < WIDTH / 2  - (SPACESHIP_HEIGHT + 10): #right
			yellow.x += VEL 

		if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - SPACESHIP_WIDTH: #down
			yellow.y += VEL 	

def handle_red_movement(keys_pressed , red):
		if keys_pressed[pygame.K_LEFT] and red.x -  VEL > (WIDTH / 2 ) - (SPACESHIP_HEIGHT - 10): #LEFT
			red.x -= VEL 
		
		if keys_pressed[pygame.K_UP] and red.y - VEL > 0 : #up
			red.y -= VEL 

		if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH - SPACESHIP_HEIGHT: #right
			red.x += VEL 

		if keys_pressed[pygame.K_DOWN] and red.y + VEL < HEIGHT - SPACESHIP_WIDTH: #down
			red.y += VEL 	

def main():
	red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
	yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
	run = True
	clock = pygame.time.Clock()	

	while run : 
		
		clock.tick(FPS)
		for event in pygame.event.get():
				if event.type == pygame.QUIT: #this is checking if the user quit the event or not
						run = False
		keys_pressed = pygame.key.get_pressed()


		handle_yellow_movement(keys_pressed,yellow)
		handle_red_movement(keys_pressed,red)







		draw_window(yellow,red)
		
	pygame.quit()

if __name__ == "__main__": #this is making sure , we can only run this function directly , we can also run by importing in python but it won't allow that 
	main()