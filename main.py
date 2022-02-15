import pygame
pygame.init()
from game import Game

#Titre du jeu
pygame.display.set_caption("Murphy is online")

#Fond d'écran et dimension de la fenêtre
screen = pygame.display.set_mode((1200,591))
background = pygame.image.load('background.png')

#Chargement du jeu
game = Game()

#Ecran d'acceuil
menu = pygame.image.load('menu.png')

#Bouttons de l'écran d'acceuil
continuer = pygame.image.load('continuer.png').convert_alpha()
nouvellepartie = pygame.image.load('nouvellepartie.png').convert_alpha()

#Curseur
curseur = pygame.image.load('curseur.png')

#classe pour les boutons à déplacer

class Bouton():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#Creation instances boutons
bouton_continuer = Bouton(443, 376, continuer)
bouton_nouvellepartie = Bouton(443, 470, nouvellepartie)

#Pendant que le logiciel tourne
running = True
while running:

    bouton_continuer.draw()
    bouton_nouvellepartie.draw()
    #Application du menu du jeu

    is_playing = False

    while is_playing == False :


        screen.blit(menu, (0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

    #Application de la fenêtre du jeu
    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    # Application du curseur
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    screen.blit(nouvellepartie, (x, y))

    #Mise à jour de l'écran
    pygame.display.flip()

    #La fenêtre reste ouverte jusqu'à ce que l'utilisateur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

