import pygame
pygame.init()
from telechargement_images import *
from classes import *

#Creation instances boutons
bouton_continuer = Bouton(443, 376, continuer)
bouton_nouvellepartie = Bouton(443, 470, nouvellepartie)


def defmenu():

	screen.fill((0,0,0))

	screen.blit(menu, (0,0))
	if bouton_continuer.draw() == True :
		is_playing = True
	if bouton_nouvellepartie.draw() == True :
		is_playing = True	

	pygame.mouse.set_visible(False)
	x, y = pygame.mouse.get_pos()
	screen.blit(curseur,(x,y))

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
