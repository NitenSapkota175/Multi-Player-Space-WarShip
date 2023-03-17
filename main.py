import pygame
import os

WIDTH , HEIGHT = 900 ,500   # depends on  your screen resolution if you are in a low resolution screen it might take huge chucks of your window  
WIN = pygame.display.set_mode((WIDTH,HEIGHT))  # here there is a tuple in display.set_mode((tuple))

#VELOCITY 
VEL = 5
FPS = 60
# bullets velocity 

BULLET_VEL = 7 

# Max number of bullets

MAX_BULLETS = 3

## Creating an event

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


# to set the window name 
pygame.display.set_caption("Spaceship war")

#images 
YELLOW_SPACESHIP_IMAGE =  pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
RED_SPACESHIP_IMAGE =  pygame.image.load(os.path.join('Assets','spaceship_red.png'))

# resize spaceships
SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55 , 40
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP =  pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)


## background image 

SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets","space.png")) , (WIDTH,HEIGHT))

##

BOARDER = pygame.Rect(WIDTH // 2 - 5 , 0 , 10 , HEIGHT )
WHITE  = (255,255,255)
BLACK = (0,0,0,0)
RED =  (255,0,0)
YELLOW = (255,255,0)

def draw_window(yellow,red,red_bullets,yellow_bullets):
	WIN.blit(SPACE,(0,0))
	pygame.draw.rect(WIN,BLACK,BOARDER)
	WIN.blit(YELLOW_SPACESHIP,(yellow.x , yellow.y))
	WIN.blit(RED_SPACESHIP,(red.x ,red.y))

	for bullet in red_bullets:
		pygame.draw.rect(WIN,RED,bullet)


	for bullet in yellow_bullets:
		pygame.draw.rect(WIN,YELLOW,bullet)	

	pygame.display.update()

def handle_yellow_movement(keys_pressed , yellow):
		if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #LEFT
			yellow.x -= VEL 
		
		if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
			yellow.y -= VEL 

		if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width  < BOARDER.x : #right
			yellow.x += VEL 

		if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - SPACESHIP_WIDTH: #down
			yellow.y += VEL 	

def handle_red_movement(keys_pressed , red):
		if keys_pressed[pygame.K_LEFT] and red.x -  VEL > BOARDER.x + BOARDER.width: #LEFT
			red.x -= VEL 
		
		if keys_pressed[pygame.K_UP] and red.y - VEL > 0 : #up
			red.y -= VEL 

		if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH - SPACESHIP_HEIGHT: #right
			red.x += VEL 

		if keys_pressed[pygame.K_DOWN] and red.y + VEL < HEIGHT - SPACESHIP_WIDTH: #down
			red.y += VEL 	
def handle_bullets(yellow_bullets,red_bullets,yellow,red):
	for bullet in yellow_bullets:
		bullet.x += BULLET_VEL # move right

		if red.colliderect(bullet):
			pygame.event.post(pygame.event.Event(RED_HIT))
			yellow_bullets.remove(bullet)

		elif bullet.x > WIDTH:
			yellow_bullets.remove(bullet)


	for bullet in red_bullets:
		bullet.x -= BULLET_VEL # move left
		if yellow.colliderect(bullet): ## collide check 
			pygame.event.post(pygame.event.Event(YELLOW_HIT))
			red_bullets.remove(bullet)

		elif bullet.x < 0:
			red_bullets.remove(bullet)


			
def main():
	red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
	yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
	red_bullets = []
	yellow_bullets = []
	run = True
	clock = pygame.time.Clock()	

	while run : 
		
		clock.tick(FPS)
		for event in pygame.event.get():
				if event.type == pygame.QUIT: #this is checking if the user quit the event or not
						run = False
		
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LCTRL and  len(yellow_bullets) < MAX_BULLETS:
						bullet = pygame.Rect(yellow.x + yellow.width , yellow.y + yellow.height // 2 - 2 , 10 , 5)
						yellow_bullets.append(bullet) 
		
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RCTRL and  len(red_bullets) < MAX_BULLETS:
						bullet = pygame.Rect(red.x , red.y + red.height // 2 - 2 , 10 , 5)
						red_bullets.append(bullet) 
				
		
		keys_pressed = pygame.key.get_pressed()


		handle_yellow_movement(keys_pressed,yellow)
		handle_red_movement(keys_pressed,red)



		handle_bullets(yellow_bullets,red_bullets,yellow,red)



		draw_window(yellow,red,red_bullets,yellow_bullets)
		
	pygame.quit()

if __name__ == "__main__": #this is making sure , we can only run this function directly , we can also run by importing in python but it won't allow that 
	main()