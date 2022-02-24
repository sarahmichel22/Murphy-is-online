import pygame
pygame.init()
from menu import *
from telechargement_images import *
from classes import *
from textes import *
from sons import *


#Pendant que le logiciel tourne
running = True
is_playing = False
navigateur = False
dossier = False
messagerie = False
notes = False
calendrier = False
parametres = False
image = 0
ispage1 = True
ispage2 = False

while running:

    screen.fill((0,0,0))

    while is_playing == False :
        screen.fill((0,0,0))
        sonmenu.play()
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


    #Application de la fenêtre du jeu
    
    screen.blit(background, (0,0))

    sonmenu.stop()
    
    #Application des icones
    if bouton_navigateur.draw() == True :
        navigateur = True

    if navigateur == True:
        screen.blit(fenetre, (234,60))
        screen.blit(titrenavigateur, (300,67))
        screen.blit(iconenavigateur, (259,65))
        if ispage2 == True:
            screen.blit(onglet1, (234, 96))
            screen.blit(blanc,(333,150))
            screen.blit(page1, (260,199))
            screen.blit(titrerecherche1,(340,160))
        elif ispage1:
            screen.blit(onglet2, (234,96))
            screen.blit(blanc,(333,150))
            screen.blit(page2, (260,199))
            screen.blit(titrerecherche2,(340,160))
        if bouton_onglet1.draw() == True:
            ispage2=True
            ispage1=False
        if bouton_onglet2.draw() == True:
            ispage1 = True
            ispage2 = False
        if bouton_croix.draw() == True :
            navigateur = False

    if bouton_dossier.draw() == True:
        dossier = True

    if dossier == True:
        screen.blit(fenetre, (234,60))
        screen.blit(ombre, (395,470))
        screen.blit(titredossier, (300,67))
        screen.blit(iconedossier, (259,65))
        screen.blit(images[image], (355,148))
        screen.blit(titresimages[image],(355,120))
        if bouton_flechedroite.draw() == True :
            if image < 6:
                image += 1
            else:
                image = 0
        if bouton_flechegauche.draw() == True :
            if image > 0:
                image -= 1
            else:
                image = 6
        if bouton_croix.draw() == True :
            dossier = False


    if bouton_messagerie.draw() == True:
        messagerie = True

    if messagerie == True:
        screen.blit(fenetre, (234,60))
        screen.blit(titremessagerie, (300,67))
        screen.blit(iconemessagerie, (259,65))
        if bouton_croix.draw() == True :
            messagerie = False

    if bouton_notes.draw() == True:
        notes = True

    if notes == True:
        screen.blit(fenetre, (234,60))
        screen.blit(titrenotes, (300,67))
        screen.blit(iconenotes, (259,65))
        if bouton_croix.draw() == True :
            notes = False

    if bouton_parametres.draw() == True:
        parametres = True

    if parametres == True:
        screen.blit(fenetre, (234,60))
        screen.blit(titreparametres, (300,67))
        screen.blit(iconeparametres, (259,65))
        if bouton_croix.draw() == True :
            parametres = False

    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    screen.blit(curseur,(x,y))


    #Mise à jour de l'écran
    pygame.display.flip()

    #La fenêtre reste ouverte jusqu'à ce que l'utilisateur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

pygame.quit()

# Application du curseur

