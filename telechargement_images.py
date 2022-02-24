import pygame
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 591

#Titre du jeu
pygame.display.set_caption("Murphy is online")

#Fond d'écran et dimension de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((0,0,0))
background = pygame.image.load("background.png")

#Curseur
curseur = pygame.image.load('curseur.png')

#Ecran d'acceuil
menu = pygame.image.load('menu.png')

#Bouttons de l'écran d'acceuil
continuer = pygame.image.load('boutons/continuer.png')
nouvellepartie = pygame.image.load('boutons/nouvellepartie.png')
curseur = pygame.image.load('curseur.png')

#Fenêtre application
fenetre = pygame.image.load('fenetre.png')
croix = pygame.image.load('boutons/croix.png')

#Boutons application
navigateur = pygame.image.load('boutons/navigateur.png')
dossier = pygame.image.load('boutons/dossier.png')
messagerie = pygame.image.load('boutons/messagerie.png')
notes = pygame.image.load('boutons/notes.png')
parametres = pygame.image.load('boutons/parametres.png')
flechedroite = pygame.image.load('dossier/flechedroite.png')
flechegauche = pygame.image.load('dossier/flechegauche.png')

#Icones applications
iconenavigateur = pygame.image.load('icones/la-terre.png')
iconedossier = pygame.image.load('icones/galerie.png')
iconemessagerie = pygame.image.load('icones/e-mail.png')
iconenotes = pygame.image.load('icones/livre.png')
iconeparametres = pygame.image.load('icones/reglage.png')

#Textes applications

#Images galerie
image1 = pygame.image.load('dossier/image1.jpeg')
image2 = pygame.image.load('dossier/image2.jpeg')
image3 = pygame.image.load('dossier/image3.jpeg')
image4 = pygame.image.load('dossier/image4.jpeg')
image5 = pygame.image.load('dossier/image5.jpeg')
image6 = pygame.image.load('dossier/image6.jpeg')
image7 = pygame.image.load('dossier/image7.jpeg')
images = [image1,image2,image3,image4,image5,image6,image7]
ombre = pygame.image.load('dossier/ombre.png')

#Images navigateur
page1 = pygame.image.load('navigateur/page1.png')
page2 = pygame.image.load('navigateur/page2.png')
onglet1 = pygame.image.load('navigateur/onglet1.png')
onglet2 = pygame.image.load('navigateur/onglet2.png')
blanc = pygame.image.load('navigateur/blanc.png')