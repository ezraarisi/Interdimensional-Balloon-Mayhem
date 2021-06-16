import pygame, time, os, sys, random
from pygame import mixer

pygame.init()
pygame.font.init()
mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
os.environ['SDL_VIDEO_CENTERED'] = '1'

barPos      = (28, 450)
barSize     = (200, 20)
borderColor = (0, 0, 0)
barColor    = (0, 128, 0)
max_a = 350

pygame.display.set_caption("Jerry's Game - Rick and Morty Challenge Code")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

def DrawBar(pos, size, borderC, barC, progress):
    pygame.draw.rect(screen, borderC, (*pos, *size), 1)
    innerPos  = (pos[0]+3, pos[1]+3)
    innerSize = ((size[0]-6) * progress, size[1]-6)
    pygame.draw.rect(screen, barC, (*innerPos, *innerSize))

screen = pygame.display.set_mode((500,500),pygame.NOFRAME)

splash = True
while splash:
	pic = pygame.image.load("assets/background_image.png")
	screen.blit(pic, (0,0))
	for a in range(350):
		# time.sleep(0.01)
		DrawBar(barPos, barSize, borderColor, barColor, a/max_a)
		screen.blit(pygame.font.Font('assets/genera.ttf', 15).render("Loading...", 1, (0, 0, 0)), (28, 470))
		pygame.display.update()
	pygame.display.flip()
	splash = False
	for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				splash = False

screen2 = pygame.display.set_mode((800,600))

instructions = True
while instructions:
	button = pygame.Rect(126, 512, 593, 723)
	pic2 = pygame.image.load("assets/background_image2.png")
	screen2.blit(pic2, (0,0))
	pygame.display.update()
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			instructions = False
			pygame.quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				# print(event.pos)
				if button.collidepoint(event.pos):
					instructions = False
					pygame.display.flip()

mixer.music.load('assets/background_music.mp3')
mixer.music.play(-1)

#Drawing
x_list = [x for x in range(680)]
bx = random.randint(1, 680)
by = 600
by_change = 4
score_value = 0
score_x, score_y = 10, 10
counter, previous_counter = 0, 0
font = pygame.font.Font('freesansbold.ttf', 32)
rballoon = pygame.image.load("assets/red.png")

def scoreboard(x, y):
	score = font.render("Score: " + str(score_value), True, (255, 255, 255))
	screen2.blit(score, (x, y))

main_game = True
while main_game:
	game_background = pygame.image.load('assets/game_background.jpg').convert()
	screen2.blit(game_background, (0, 0))
	screen2.blit(rballoon, (bx, by))
	by -= by_change
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			main_game = False
		balloon_rect = rballoon.get_rect(topleft=(bx, by))
		# print(type(balloon_rect))
		if event.type == pygame.MOUSEBUTTONDOWN and balloon_rect.collidepoint(event.pos):
			pop_sound = mixer.Sound('assets/pop.wav')
			pop_sound.play()
			score_value += 1
			by = 620
			random.shuffle(x_list)
			bx = random.choice(x_list)

	scoreboard(10, 10)
	pygame.display.update()
pygame.quit()
