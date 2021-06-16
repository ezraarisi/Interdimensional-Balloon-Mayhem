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

#Balloons
balloon = []
balloon_x = []
balloon_y = []
bal_list = ['assets/red.png', 'assets/blue.png', 'assets/yellow.png', 'assets/green.png']
balloon_y_change = []
balloons = 4

#Other variables
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('assets/smith.ttf', 60)
score_value = 0
score_x, score_y = 10, 10

for count, bal in enumerate(bal_list):
	balloon.append(pygame.image.load(str(bal_list[count])))
	balloon_x.append(random.randint(0, 680))
	balloon_y.append(random.randint(600, 700))
	balloon_y_change.append(random.randint(1, 4))

x = [abs(j-i) for i, j in zip(balloon_x[:-1], balloon_x[1:])]
for count, a in enumerate(x):
	if a > 60:
		balloon_x[count] = random.randint(0, 680)

def draw_balloons(i, x, y):
	screen2.blit(balloon[i], (x, y))

def game_over_text():
    over_text = font2.render("GAME OVER!", True, (255, 255, 255))
    screen2.blit(over_text, (200, 250))

def scoreboard(x, y):
	score = font.render("Score: " + str(score_value), True, (255, 255, 255))
	screen2.blit(score, (x, y))

#Balloon pop
def balloon_pop(x, y):
	balloon_rect = balloon[i].get_rect(topleft=(x, y))

	if balloon_rect.collidepoint(pygame.mouse.get_pos()):
		return True
	else:
		return False

main_game = True
end = False
while main_game:
	game_background = pygame.image.load('assets/game_background.jpg').convert()
	screen2.blit(game_background, (0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			main_game = False
			pygame.quit()
			sys.exit()

	for i in range(balloons):
		if balloon_y[i] < 20:
			for j in range(balloons):
				balloon_y[j] = 2000
				end = True

		balloon_y[i] -= balloon_y_change[i]
		balloon_pop_bool = balloon_pop(balloon_x[i], balloon_y[i])
		draw_balloons(i, balloon_x[i], balloon_y[i])
		if balloon_pop_bool and event.type == pygame.MOUSEBUTTONDOWN: 
			pop_sound = mixer.Sound('assets/pop.wav')
			pop_sound.play()
			score_value += 1
			balloon_y[i] = random.randint(600, 700)
			balloon_x[i] = random.randint(0, 680)
			for k in range(balloons):
				if abs(balloon_x[i] - balloon_x[k]) <= 60:
					balloon_x[i] = random.randint(0, 680)
			continue
		

	scoreboard(10, 10)
	if end == True:
		screen2.blit(game_background, (0, 0))
		game_over_text()
		mixer.music.stop()
	pygame.display.update()

