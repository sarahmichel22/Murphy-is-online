import pygame
pygame.init()
from menu import *
from telechargement_images import *
from classes import *
from textes import *
from sons import *
from messagerie import *
from conversationPolice import *
from conversationVictoria import *
from notes import *

running = True
is_playing = False
navigateur = False
dossier = False
messagerie = False
contacts = True
notes = False
calendrier = False
parametres = False
image = 0
ispage1 = True
ispage2 = False
musique = 1
son = 1
notes_debloquees = False
chiffre1 = 10
chiffre2 = 10
chiffre3 = 10
chiffre4 = 10
derniermessagePolice = len(conversationPolice)-1
derniermessageVictoria = len(conversationVictoria)-1


#Pendant que le logiciel tourne


from notes import *

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

#################################################################################################################################
    
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

#################################################################################################################################

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

##########################################################################################################################

    if bouton_messagerie.draw() == True:
        messagerie = True

    if messagerie == True:

        screen.blit(fenetre, (234,60))
        screen.blit(titremessagerie, (300,67))
        screen.blit(iconemessagerie, (259,65))

        if contacts == True :
            if bouton_Susan.draw() == True:
                Susan = True
                contacts = False
            screen.blit(nomSusan,(375,260))
            if bouton_Noah.draw() == True:
                Noah = True
                contacts = False
            screen.blit(nomNoah,(780,260))
            if bouton_Victoria.draw() == True:
                Victoria = True
                contacts = False
            screen.blit(nomVictoria,(570,260))
            if bouton_Police.draw() == True:
                Police = True
                contacts = False
            screen.blit(nomPolice,(575,460))
            if bouton_DrDavies.draw() == True:
                DrDavies = True
                contacts = False
            screen.blit(nomDrDavies,(765,460))
            if bouton_Taylor.draw() == True:
                Taylor = True
                contacts = False
            screen.blit(nomTaylor,(375,460))
            
        else :
            screen.blit(boitemessagerie,(255,110))
            if bouton_retour.draw():
                contacts = True
                Susan = False
                Noah = False
                Victoria = False
                Taylor = False
                Police = False
                DrDavies = False

            nomcontacts()
            if Susan == True:
                screen.blit(nomSusan, (250,220))
                screen.blit(photoSusan, (250,115))
            if Noah == True:
                screen.blit(nomNoah, (250,220))
                screen.blit(photoNoah, (250,115))
                screen.blit(conversationNoah[derniermessageNoah-4],(380,140))
                screen.blit(conversationNoah[derniermessageNoah-3],(380,170))
                screen.blit(conversationNoah[derniermessageNoah-2],(380,200))
                screen.blit(conversationNoah[derniermessageNoah-1],(380,230))
                screen.blit(conversationNoah[derniermessageNoah],(380,260))
                if bouton_flechehaut.draw() == True and not derniermessageNoah<5:
                    derniermessageNoah-=1
                if bouton_flechebas.draw() == True and derniermessageNoah!=(len(conversationVictoria)-1):
                    derniermessageNoah+=1
            if Victoria == True:
                screen.blit(nomVictoria, (250,220))
                screen.blit(photoVictoria, (250,115))
                screen.blit(conversationVictoria[derniermessageVictoria-4],(380,140))
                screen.blit(conversationVictoria[derniermessageVictoria-3],(380,170))
                screen.blit(conversationVictoria[derniermessageVictoria-2],(380,200))
                screen.blit(conversationVictoria[derniermessageVictoria-1],(380,230))
                screen.blit(conversationVictoria[derniermessageVictoria],(380,260))
                if bouton_flechehaut.draw() == True and not derniermessageVictoria<5:
                    derniermessageVictoria-=1
                if bouton_flechebas.draw() == True and derniermessageVictoria!=(len(conversationVictoria)-1):
                    derniermessageVictoria+=1
            if Taylor == True:
                screen.blit(nomTaylor, (250,220))
                screen.blit(photoTaylor, (250,115))
                #affichermessages(conversationTaylor)
            if Police == True:
                screen.blit(nomPolice, (250,220))
                screen.blit(photoPolice, (250,115))
                screen.blit(conversationPolice[derniermessagePolice-4],(380,140))
                screen.blit(conversationPolice[derniermessagePolice-3],(380,170))
                screen.blit(conversationPolice[derniermessagePolice-2],(380,200))
                screen.blit(conversationPolice[derniermessagePolice-1],(380,230))
                screen.blit(conversationPolice[derniermessagePolice],(380,260))
                if bouton_flechehaut.draw() == True and not derniermessagePolice<5:
                    derniermessagePolice-=1
                if bouton_flechebas.draw() == True and derniermessagePolice!=(len(conversationPolice)-1):
                    derniermessagePolice+=1
                
            if DrDavies == True:
                screen.blit(nomDrDavies, (250,220))
                screen.blit(photoDrDavies, (250,115))
                #affichermessages(conversationDrDavies)
            screen.blit(photoMurphy, (250,337))

        if bouton_croix.draw() == True :
            messagerie = False

##########################################################################################################################

    if bouton_notes.draw() == True:
        notes = True

    if notes == True:
        screen.blit(fenetre, (234,60))
        screen.blit(titrenotes, (300,67))
        screen.blit(iconenotes, (259,65))
        if notes_debloquees == False:

            screen.blit(mdpnotes, (425, 130))
            screen.blit(traitnombre, (435,190))
            screen.blit(traitnombre, (515,190))
            screen.blit(traitnombre, (595,190))
            screen.blit(traitnombre, (675,190))

            if bouton_zero.draw() == True:
                if chiffre1 > 9:
                    chiffre1 = 0
                elif chiffre2 > 9:
                    chiffre2 = 0
                elif chiffre3 > 9:
                    chiffre3 = 0
                elif chiffre4 > 9:
                    chiffre4 = 0

            if bouton_un.draw() == True:
                if chiffre1 > 9:
                    chiffre1 = 1
                elif chiffre2 > 9:
                    chiffre2 = 1
                elif chiffre3 > 9:
                    chiffre3 = 1
                elif chiffre4 > 9:
                    chiffre4 = 1

            if bouton_deux.draw() == True:
                if chiffre1 > 9:
                    chiffre1 = 2
                elif chiffre2 > 9:
                    chiffre2 = 2
                elif chiffre3 > 9:
                    chiffre3 = 2
                elif chiffre4 > 9:
                    chiffre4 = 2

            if bouton_trois.draw() == True:
                if chiffre1 > 9:
                    chiffre1 = 3
                elif chiffre2 > 9:
                    chiffre2 = 3
                elif chiffre3 > 9:
                    chiffre3 = 3
                elif chiffre4 > 9:
                    chiffre4 = 3

            if bouton_quatre.draw() == True:
                if chiffre1 > 9:
                    chiffre1 = 4
                elif chiffre2 > 9:
                    chiffre2 = 4
                elif chiffre3 > 9:
                    chiffre3 = 4
                elif chiffre4 > 9:
                    chiffre4 = 4

            if bouton_cinq.draw() == True:
                if chiffre1 > 9:
                    chiffre1 = 5
                elif chiffre2 > 9:
                    chiffre2 = 5
                elif chiffre3 > 9:
                    chiffre3 = 5
                elif chiffre4 > 9:
                    chiffre4 = 5

            if bouton_six.draw() == True:
                if chiffre1 > 9:
                    chiffre1 = 6
                elif chiffre2 > 9:
                    chiffre2 = 6
                elif chiffre3 > 9:
                    chiffre3 = 6
                elif chiffre4 > 9:
                    chiffre4 = 6

            if bouton_sept.draw() == True:
                if chiffre1 > 9:
                    chiffre1 = 7
                elif chiffre2 > 9:
                    chiffre2 = 7
                elif chiffre3 > 9:
                    chiffre3 = 7
                elif chiffre4 > 9:
                    chiffre4 = 7

            if bouton_huit.draw() == True:
                if chiffre1 > 9:
                    chiffre1 = 8
                elif chiffre2 > 9:
                    chiffre2 = 8
                elif chiffre3 > 9:
                    chiffre3 = 8
                elif chiffre4 > 9:
                    chiffre4 = 8

            if bouton_neuf.draw() == True:
                if chiffre1 > 9:
                    chiffre1 = 9
                elif chiffre2 > 9:
                    chiffre2 = 9
                elif chiffre3 > 9:
                    chiffre3 = 9
                elif chiffre4 > 9:
                    chiffre4 = 9

            if bouton_annuler.draw() == True:
                if chiffre4<10:
                    chiffre4=10
                elif chiffre3<10:
                    chiffre3=10
                elif chiffre2<10:
                    chiffre2=10 
                elif chiffre1<10:
                    chiffre1=10
            if bouton_valider.draw()== True:
                if validermdp(chiffre1,chiffre2,chiffre3,chiffre4)==True:
                    notes_debloquees = True
            afficherChiffres(chiffre1,chiffre2,chiffre3,chiffre4,screen)
            
            
        if bouton_croix.draw() == True :
            notes = False

##########################################################################################################################

    if bouton_parametres.draw() == True:
        parametres = True

    if parametres == True:

        screen.blit(fenetre, (234,60))
        screen.blit(titreparametres, (300,67))
        screen.blit(iconeparametres, (259,65))

        if bouton_plus1.draw() == True:
            if musique == 0:
                musique = 0.3
            elif musique == 0.3:
                musique = 0.6
            elif musique == 0.6:
                musique = 1
        if bouton_moins1.draw() == True:
            if musique == 1:
                musique = 0.6
            elif musique == 0.6:
                musique = 0.3
            elif musique == 0.3:
                musique = 0

        if bouton_plus2.draw() == True:
            if son == 0:
                son = 0.3
            elif son == 0.3:
                son = 0.6
            elif son == 0.6:
                son = 1
        if bouton_moins2.draw() == True:
            if son == 1:
                son = 0.6
            elif son == 0.6:
                son = 0.3
            elif son == 0.3:
                son = 0

#################################################################################################################################

        sonmenu.set_volume(musique)
        sonclic.set_volume(son)
        
        if musique == 1:
            screen.blit(volumehaut,(600,133))
        if musique == 0.6:
            screen.blit(volumemoyen,(600,133))
        if musique == 0.3:
            screen.blit(volumebas,(600,133))
        if musique == 0:
            screen.blit(volumemuet,(600,133))

        if son == 1:
            screen.blit(volumehaut,(520,233))
        if son == 0.6:
            screen.blit(volumemoyen,(520,233))
        if son == 0.3:
            screen.blit(volumebas,(520,233))
        if son == 0:
            screen.blit(volumemuet,(520,233))

        screen.blit(volumemusique,(300,150)) 
        screen.blit(volumeson,(300,250))

        screen.blit(changerpdp,(300,350))
        screen.blit(traitbas,(298,355))
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

