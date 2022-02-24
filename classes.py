import pygame
pygame.init()
from telechargement_images import *
from sons import *
from pygame.locals import *
from textes import *

#Boutons

class Bouton():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        #Vérifie si la souris est sur un des boutons
        if self.rect.collidepoint(pos):
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    sonclic.play()
                    action = True
                
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

#Creation instances boutons
bouton_continuer = Bouton(443, 376, continuer)
bouton_nouvellepartie = Bouton(443, 470, nouvellepartie)

bouton_navigateur = Bouton(190, 540, navigateur)
bouton_dossier = Bouton(250, 539, dossier)
bouton_messagerie = Bouton(315, 537, messagerie)
bouton_notes = Bouton(380, 536, notes)
bouton_parametres = Bouton(440,539, parametres)

bouton_croix = Bouton(905, 64, croix)

bouton_flechedroite = Bouton(905, 295, flechedroite)
bouton_flechegauche = Bouton(260, 295, flechegauche)

bouton_onglet1 = Bouton(273, 113, titreonglet1)
bouton_onglet2 = Bouton(503, 113, titreonglet2)