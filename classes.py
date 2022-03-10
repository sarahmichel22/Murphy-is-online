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

bouton_flechedroite = Bouton(870, 280, flechedroite)
bouton_flechegauche = Bouton(260, 280, flechegauche)

bouton_onglet1 = Bouton(273, 113, titreonglet1)
bouton_onglet2 = Bouton(503, 113, titreonglet2)

#Paramètres
bouton_plus1 = Bouton(670,149,plus)
bouton_moins1 = Bouton(560,149,moins)
bouton_plus2 = Bouton(590,249,plus)
bouton_moins2 = Bouton(480,249,moins)

#Notes
bouton_un = Bouton(500,280,un)
bouton_deux = Bouton(560,280,deux)
bouton_trois = Bouton(620,280,trois)
bouton_quatre = Bouton(500,340,quatre)
bouton_cinq = Bouton(560,340,cinq)
bouton_six = Bouton(620,340,six)
bouton_sept = Bouton(500,400,sept)
bouton_huit = Bouton(560,400,huit)
bouton_neuf = Bouton(620,400,neuf)
bouton_zero = Bouton(560,460,zero)

#Messagerie
bouton_retour = Bouton(860,64,retour)
bouton_flechehaut = Bouton(880,120,flechehaut)
bouton_flechebas = Bouton(880,302,flechebas)

#Contacts
bouton_Susan = Bouton(345,150,photoSusan)
bouton_Victoria = Bouton(545,150,photoVictoria)
bouton_Noah = Bouton(745,150,photoNoah)
bouton_Taylor = Bouton(345,350,photoTaylor)
bouton_Police = Bouton(545,350,photoPolice)
bouton_DrDavies = Bouton(745,350,photoDrDavies)
