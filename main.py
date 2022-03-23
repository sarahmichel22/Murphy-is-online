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
from conversationNoah import *
from conversationDrDavies import *
from conversationTaylor import *
from conversationSusan import *
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
derniermessageNoah = len(conversationNoah)-1
derniermessagePolice = len(conversationPolice)-1
derniermessageVictoria = len(conversationVictoria)-1
derniermessageDrDavies = len(conversationDrDavies)-1
derniermessageTaylor = len(conversationTaylor)-1
derniermessageSusan = len(conversationSusan)-1
premierenote = 0
Susan = False
Noah = False
Victoria = False
DrDavies = False
Taylor = False
Police = False
messagePolicefin = False
bonnefin = False
finhopital = False
finsuicide = False


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
                notificationSusan = False
            screen.blit(nomSusan,(365,260))
            if avancementhistoire < 8:
                screen.blit(boutonhorsligne,(410,259))
            else :
                screen.blit(boutonenligne,(410,259))
            if bouton_Noah.draw() == True:
                Noah = True
                contacts = False
                notificationNoah = False
            screen.blit(nomNoah,(770,260))
            if avancementhistoire < 8:
                screen.blit(boutonenligne,(808,259))
            else :
                screen.blit(boutonhorsligne,(808,259))
            if bouton_Victoria.draw() == True:
                Victoria = True
                contacts = False
                notificationVictoria = False
            screen.blit(nomVictoria,(560,260))
            screen.blit(boutonhorsligne,(615,259))
            if bouton_Police.draw() == True:
                Police = True
                contacts = False
                notificationPolice = False
            screen.blit(nomPolice,(565,460))
            if notes_debloquees ==True:
                screen.blit(boutonenligne,(610,459))
            else :
                screen.blit(boutonhorsligne,(610,459))
            if bouton_DrDavies.draw() == True:
                DrDavies = True
                contacts = False
                notificationDrDavies = False
            screen.blit(nomDrDavies,(755,460))
            screen.blit(boutonhorsligne,(820,459))

            if bouton_Taylor.draw() == True:
                Taylor = True
                contacts = False
                notificationTaylor = False
            screen.blit(nomTaylor,(365,460))
            screen.blit(boutonhorsligne,(410,459))

            notificationContact(screen,notificationcontact,notificationSusan,notificationNoah,notificationPolice,notificationVictoria,notificationTaylor,notificationDrDavies)
            
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
                screen.blit(horsligneSusan,(380,355))
                screen.blit(horsligne,(380,385))
                if avancementhistoire >= 9 and avancementhistoire < 18 :
                    screen.blit(boitemessageriereponse,(255,344))
                    screen.blit(boutonenligne,(296,219))
                else:
                    screen.blit(boutonhorsligne,(296,219))
                screen.blit(conversationSusan[derniermessageSusan-6],(380,132))
                screen.blit(conversationSusan[derniermessageSusan-5],(380,162))
                screen.blit(conversationSusan[derniermessageSusan-4],(380,192))
                screen.blit(conversationSusan[derniermessageSusan-3],(380,222))
                screen.blit(conversationSusan[derniermessageSusan-2],(380,252))
                screen.blit(conversationSusan[derniermessageSusan-1],(380,282))
                screen.blit(conversationSusan[derniermessageSusan],(380,312))
                if bouton_flechehaut.draw() == True and not derniermessageSusan<7:
                    derniermessageSusan-=1
                if bouton_flechebas.draw() == True and derniermessageSusan!=(len(conversationSusan)-1):
                    derniermessageSusan+=1
                
            if Noah == True:
                screen.blit(nomNoah, (250,220))
                screen.blit(photoNoah, (250,115))
                screen.blit(horsligneNoah,(380,355))
                screen.blit(horsligne,(380,385))
                if avancementhistoire < 9:
                    screen.blit(boitemessageriereponse,(255,344))
                    screen.blit(boutonenligne,(287,219))
                else:
                    screen.blit(boutonhorsligne,(287,219))
                screen.blit(conversationNoah[derniermessageNoah-6],(380,132))
                screen.blit(conversationNoah[derniermessageNoah-5],(380,162))
                screen.blit(conversationNoah[derniermessageNoah-4],(380,192))
                screen.blit(conversationNoah[derniermessageNoah-3],(380,222))
                screen.blit(conversationNoah[derniermessageNoah-2],(380,252))
                screen.blit(conversationNoah[derniermessageNoah-1],(380,282))
                screen.blit(conversationNoah[derniermessageNoah],(380,312))
                if bouton_flechehaut.draw() == True and not derniermessageNoah<7:
                    derniermessageNoah-=1
                if bouton_flechebas.draw() == True and derniermessageNoah!=(len(conversationNoah)-1):
                    derniermessageNoah+=1

            if Victoria == True:
                screen.blit(nomVictoria, (250,220))
                screen.blit(photoVictoria, (250,115))
                screen.blit(horsligneVictoria,(380,355))
                screen.blit(horsligne,(380,385))
                screen.blit(boutonhorsligne,(305,219))
                screen.blit(conversationVictoria[derniermessageVictoria-6],(380,132))
                screen.blit(conversationVictoria[derniermessageVictoria-5],(380,162))
                screen.blit(conversationVictoria[derniermessageVictoria-4],(380,192))
                screen.blit(conversationVictoria[derniermessageVictoria-3],(380,222))
                screen.blit(conversationVictoria[derniermessageVictoria-2],(380,252))
                screen.blit(conversationVictoria[derniermessageVictoria-1],(380,282))
                screen.blit(conversationVictoria[derniermessageVictoria],(380,312))
                if bouton_flechehaut.draw() == True and not derniermessageVictoria<7:
                    derniermessageVictoria-=1
                if bouton_flechebas.draw() == True and derniermessageVictoria!=(len(conversationVictoria)-1):
                    derniermessageVictoria+=1

            if Taylor == True:
                screen.blit(nomTaylor, (250,220))
                screen.blit(photoTaylor, (250,115))
                screen.blit(horsligneTaylor,(380,355))
                screen.blit(horsligne,(380,385))
                screen.blit(boutonhorsligne,(298,219))
                screen.blit(conversationTaylor[derniermessageTaylor-6],(380,132))
                screen.blit(conversationTaylor[derniermessageTaylor-5],(380,162))
                screen.blit(conversationTaylor[derniermessageTaylor-4],(380,192))
                screen.blit(conversationTaylor[derniermessageTaylor-3],(380,222))
                screen.blit(conversationTaylor[derniermessageTaylor-2],(380,252))
                screen.blit(conversationTaylor[derniermessageTaylor-1],(380,282))
                screen.blit(conversationTaylor[derniermessageTaylor],(380,312))
                if bouton_flechehaut.draw() == True and not derniermessageTaylor<7:
                    derniermessageTaylor-=1
                if bouton_flechebas.draw() == True and derniermessageTaylor!=(len(conversationTaylor)-1):
                    derniermessageTaylor+=1

            if Police == True:
                screen.blit(nomPolice, (250,220))
                screen.blit(photoPolice, (250,115))
                screen.blit(horslignePolice,(380,355))
                screen.blit(horsligne,(380,385))
                screen.blit(boutonhorsligne,(296,219))
                screen.blit(conversationPolice[derniermessagePolice-6],(380,132))
                screen.blit(conversationPolice[derniermessagePolice-5],(380,162))
                screen.blit(conversationPolice[derniermessagePolice-4],(380,192))
                screen.blit(conversationPolice[derniermessagePolice-3],(380,222))
                screen.blit(conversationPolice[derniermessagePolice-2],(380,252))
                screen.blit(conversationPolice[derniermessagePolice-1],(380,282))
                screen.blit(conversationPolice[derniermessagePolice],(380,312))
                if bouton_flechehaut.draw() == True and not derniermessagePolice<7:
                    derniermessagePolice-=1
                if bouton_flechebas.draw() == True and derniermessagePolice!=(len(conversationPolice)-1):
                    derniermessagePolice+=1
                if notes_debloquees == True:
                    screen.blit(boitemessageriereponse,(255,344))
                    screen.blit(boutonenligne,(296,219))

                
            if DrDavies == True:
                screen.blit(nomDrDavies, (250,220))
                screen.blit(photoDrDavies, (250,115))
                screen.blit(horsligneDrDavies,(380,355))
                screen.blit(horsligne,(380,385))
                screen.blit(boutonhorsligne,(314,219))
                screen.blit(conversationDrDavies[derniermessageDrDavies-6],(380,132))
                screen.blit(conversationDrDavies[derniermessageDrDavies-5],(380,162))
                screen.blit(conversationDrDavies[derniermessageDrDavies-4],(380,192))
                screen.blit(conversationDrDavies[derniermessageDrDavies-3],(380,222))
                screen.blit(conversationDrDavies[derniermessageDrDavies-2],(380,252))
                screen.blit(conversationDrDavies[derniermessageDrDavies-1],(380,282))
                screen.blit(conversationDrDavies[derniermessageDrDavies],(380,312))
                if bouton_flechehaut.draw() == True and not derniermessageDrDavies<7:
                    derniermessageDrDavies-=1
                if bouton_flechebas.draw() == True and derniermessageDrDavies!=(len(conversationDrDavies)-1):
                    derniermessageDrDavies+=1
            screen.blit(photoMurphy, (250,337))
            screen.blit(nomMurphy, (250,452))

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
                    messagePolicefin = True
            afficherChiffres(chiffre1,chiffre2,chiffre3,chiffre4,screen)
            
        elif notes_debloquees == True:
            
            screen.blit(notesliste[premierenote],(300,140))
            screen.blit(notesliste[premierenote+1],(300,170))
            screen.blit(notesliste[premierenote+2],(300,200))
            screen.blit(notesliste[premierenote+3],(300,230))
            screen.blit(notesliste[premierenote+4],(300,260))
            screen.blit(notesliste[premierenote+5],(300,290))
            screen.blit(notesliste[premierenote+6],(300,320))
            screen.blit(notesliste[premierenote+7],(300,350))
            screen.blit(notesliste[premierenote+8],(300,380))
            screen.blit(notesliste[premierenote+9],(300,410))
            screen.blit(notesliste[premierenote+10],(300,440))
            screen.blit(notesliste[premierenote+11],(300,470))
            if bouton_flechehaut.draw() == True and not premierenote==0:
                premierenote-=1
            if bouton_flechebas.draw() == True and not premierenote==len(notesliste)-12:
                premierenote+=1
            
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
        sonnotification.set_volume(son)
        
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

    if notificationNoah==True or notificationVictoria==True or notificationSusan==True or notificationTaylor==True or notificationPolice==True or notificationDrDavies==True:
        screen.blit(notification,(350,533))


    if avancementhistoire == 0:
        ajoutemessageAutre(messageNoah1,conversationNoah,nomMessagerieNoah)
        avancementhistoire+=1
        notificationNoah = True
        derniermessageNoah = len(conversationNoah)-1

    elif avancementhistoire == 1 and messagerie==True and Noah==True:
        affichereponses(messageNMurphy2,screen)
        if bouton_choix1.draw()== True:
            ajoutemessageMurphy(messageNMurphy2[0],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah3[0],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire+=2

        if bouton_choix2.draw()== True:
            ajoutemessageMurphy(messageNMurphy2[1],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah3[1],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire+=2

        if bouton_choix3.draw()== True:
            ajoutemessageMurphy(messageNMurphy2[2],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah3[2],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire+=2

    elif avancementhistoire == 3 and messagerie==True and Noah==True:
        affichereponses(messageNMurphy4,screen)
        if bouton_choix1.draw()== True:
            ajoutemessageMurphy(messageNMurphy4[0],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah5[0],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire=9

        if bouton_choix2.draw()== True:
            ajoutemessageMurphy(messageNMurphy4[1],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah5[1],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire+=2

        if bouton_choix3.draw()== True:
            ajoutemessageMurphy(messageNMurphy4[2],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah5[2],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire+=2

    elif avancementhistoire == 5 and messagerie==True and Noah==True:
        affichereponses(messageNMurphy6,screen)
        if bouton_choix1.draw()== True:
            ajoutemessageMurphy(messageNMurphy6[0],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah7[0],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire=9

        if bouton_choix2.draw()== True:
            ajoutemessageMurphy(messageNMurphy6[1],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah7[1],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire=9

        if bouton_choix3.draw()== True:
            ajoutemessageMurphy(messageNMurphy6[2],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah7[2],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire+=2

    elif avancementhistoire == 7 and messagerie==True and Noah==True:
        affichereponses(messageNMurphy8,screen)
        if bouton_choix1.draw()== True:
            ajoutemessageMurphy(messageNMurphy8[0],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah9[0],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire+=2

        if bouton_choix2.draw()== True:
            ajoutemessageMurphy(messageNMurphy8[1],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah9[1],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire+=2

        if bouton_choix3.draw()== True:
            ajoutemessageMurphy(messageNMurphy8[2],conversationNoah,nomMessagerieMurphy)
            derniermessageNoah = len(conversationNoah)-1
            ajoutemessageAutre(messageNoah9[2],conversationNoah,nomMessagerieNoah)
            derniermessageNoah = len(conversationNoah)-1
            avancementhistoire+=2



    elif avancementhistoire == 9:
        ajoutemessageAutre(messageSusan1,conversationSusan,nomMessagerieSusan)
        avancementhistoire+=1
        notificationSusan = True
        derniermessageSusan = len(conversationSusan)-1

    elif avancementhistoire == 10 and messagerie==True and Susan==True:
        affichereponses(messageSMurphy2,screen)
        if bouton_choix1.draw()== True:
            ajoutemessageMurphy(messageSMurphy2[0],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan3[0],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

        if bouton_choix2.draw()== True:
            ajoutemessageMurphy(messageSMurphy2[1],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan3[1],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

        if bouton_choix3.draw()== True:
            ajoutemessageMurphy(messageSMurphy2[2],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan3[2],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

    elif avancementhistoire == 12 and messagerie==True and Susan==True:
        affichereponses(messageSMurphy4,screen)
        if bouton_choix1.draw()== True:
            ajoutemessageMurphy(messageSMurphy4[0],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan5[0],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire = 18

        if bouton_choix2.draw()== True:
            ajoutemessageMurphy(messageSMurphy4[1],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan5[1],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

        if bouton_choix3.draw()== True:
            ajoutemessageMurphy(messageSMurphy4[2],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan5[2],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

    elif avancementhistoire == 14 and messagerie==True and Susan==True:
        affichereponses(messageSMurphy6,screen)
        if bouton_choix1.draw()== True:
            ajoutemessageMurphy(messageSMurphy6[0],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan7[0],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

        if bouton_choix2.draw()== True:
            ajoutemessageMurphy(messageSMurphy6[1],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan7[1],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

        if bouton_choix3.draw()== True:
            ajoutemessageMurphy(messageSMurphy6[2],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan7[2],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

    elif avancementhistoire == 16 and messagerie==True and Susan==True:
        affichereponses(messageSMurphy8,screen)
        if bouton_choix1.draw()== True:
            ajoutemessageMurphy(messageSMurphy8[0],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan9[0],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

        if bouton_choix2.draw()== True:
            ajoutemessageMurphy(messageSMurphy8[1],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan9[1],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

        if bouton_choix3.draw()== True:
            ajoutemessageMurphy(messageSMurphy8[2],conversationSusan,nomMessagerieMurphy)
            derniermessageSusan = len(conversationSusan)-1
            ajoutemessageAutre(messageSusan9[2],conversationSusan,nomMessagerieSusan)
            derniermessageSusan = len(conversationSusan)-1
            avancementhistoire+=2

    elif notes_debloquees == True and messagePolicefin == True:
        ajoutemessageAutre(messagePoliceFin,conversationPolice,nomMessageriePolice)
        avancementhistoire+=1
        notificationPolice = True
        derniermessagePolice = len(conversationPolice)-1
        messagePolicefin = False

    elif notes_debloquees == True and messagerie == True and Police == True:
        affichereponses(messagePMurphyFin,screen)
        if bouton_choix1.draw()== True:
            ajoutemessageMurphy(messagePMurphyFin[0],conversationPolice,nomMessagerieMurphy)
            derniermessagePolice = len(conversationPolice)-1
            avancementhistoire+=1
            finhopital = True

        if bouton_choix2.draw()== True:
            ajoutemessageMurphy(messagePMurphyFin[1],conversationPolice,nomMessagerieMurphy)
            derniermessagePolice = len(conversationPolice)-1
            avancementhistoire+=1
            bonnefin = True

        if bouton_choix3.draw()== True:
            ajoutemessageMurphy(messagePMurphyFin[2],conversationPolice,nomMessagerieMurphy)
            derniermessagePolice = len(conversationPolice)-1
            avancementhistoire+=1
            finhopital = True

    '''elif avancementhistoire == 19 and messagerie==True and Police==True:
        affichereponses(messagePMurphyFin,screen)
        if bouton_choix1.draw()== True:
            ajoutemessageMurphy(messagePMurphyFin[0],conversationPolice,nomMessagerieMurphy)
            derniermessagePolice = len(conversationPolice)-1
            avancementhistoire+=1

        if bouton_choix2.draw()== True:
            ajoutemessageMurphy(messagePMurphyFin[1],conversationPolice,nomMessagerieMurphy)
            derniermessagePolice = len(conversationPolice)-1
            avancementhistoire+=1

        if bouton_choix3.draw()== True:
            ajoutemessageMurphy(messagePMurphyFin[2],conversationPolice,nomMessagerieMurphy)
            derniermessagePolice = len(conversationPolice)-1
            avancementhistoire+=1
'''


    
    if bonnefin == True:
        screen.blit(imgbonnefin,(0,0))
    elif finhopital ==True:
        screen.blit(imgfinhopital,(0,0))
    elif finsuicide == True :
        screen.blit(imgfinsuicide,(0,0))







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

