import pygame
pygame.init()
from menu import *
from telechargement_images import *
from classes import *
from textes import *
from sons import *
from conversationPolice import *

avancementhistoire = 0

Susan = False
Noah = False
Victoria = False
Taylor = False
Police = False
DrDavies = False

notificationSusan = False
notificationNoah = False
notificationVictoria = False
notificationTaylor = False
notificationPolice = False
notificationDrDavies = False
derniermessageMurphyNoah = 0

def photodeprofil():

	# Photo de profil Murphy
	screen.blit(pdpbase, (250,115))

	# Photo de profil destinataire
	screen.blit(pdpbase, (250,337))

	if DrDavies == True:
		screen.blit(pdpDrDavies, (250,337))

def nomcontacts():
	if Susan == True:
		screen.blit(nomSusan, (250,230))
	if Noah == True:
		screen.blit(nomNoah, (250,230))
	if Victoria == True:
		screen.blit(nomVictoria, (250,230))
	if Taylor == True:
		screen.blit(nomTaylor, (250,230))
	if Police == True:
		screen.blit(nomPolice, (250,230))
	if DrDavies == True:
		screen.blit(nomDrDavies, (250,230))

	

def notificationContact(screen,notificationcontact,notificationSusan,notificationNoah,notificationPolice,notificationVictoria,notificationTaylor,notificationDrDavies):
	if notificationSusan == True:
		screen.blit(notificationcontact,(430,133))
	if notificationVictoria == True:
		screen.blit(notificationcontact,(630,133))
	if notificationNoah == True:
		screen.blit(notificationcontact,(830,133))
	if notificationPolice == True :
		screen.blit(notificationcontact,(630,333))

def ajoutemessageMurphy(xmessages,xconversation,nomMessagerieMurphy):
	xconversation.append(nomMessagerieMurphy)
	xconversation.append(xmessages)

def ajoutemessageAutre(xmessages,xconversation,xnom):
    xconversation.append(xnom)
    for i in xmessages:
    	xconversation.append(i)
    sonnotification.play()
    return xconversation

def affichereponses(xmessages,screen):
	screen.blit(xmessages[0],(410,370))
	screen.blit(xmessages[1],(410,410))
	screen.blit(xmessages[2],(410,450))

'''if avancementhistoire == 0:
	ajoutemessageAutre(messageNoah1,conversationNoah,nomNoah)
	avancementhistoire+=1

elif avancementhistoire = 2:
	if derniermessageMurphyNoah = 1
		ajoutemessageAutre(messageNoah1)

'''