import pygame
pygame.init()
from menu import *
from telechargement_images import *
from classes import *
from textes import *
from sons import *
from conversationPolice import *

avancementhistoire = 0

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

	screen.blit(nomMurphy, (250,452))


def ajoutemessageAutre(xmessages,xconversation,xnom):
    pygame.time.delay(10000)
    xconversation.append(xnom)
    for i in xmessages:
    	xconversation.append(i)
    sonnotification.play()
    return xconversation

if avancementhistoire = 0:
	ajoutemessageAutre(messageNoah1,conversationNoah,nomNoah)
	avancementhistoire+=1
elif avancementhistoire = 2:
	if derniermessageMurphyNoah = 1
		ajoutemessageAutre(messageNoah1)

