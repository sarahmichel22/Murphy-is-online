import pygame
pygame.init()
from menu import *
from telechargement_images import *
from classes import *
from textes import *
from sons import *
from ConversationPM import *

avancementhistoire = 0
niveaujeu = 0
affectionSusan = 70
affectionNoah = 80
affectionVictoria = 40
affectionTaylor = 30
confiancePolice = 50
confianceDrDavies = 50

notificationSusan = False
notificationNoah = False
notificationVictoria = False
notificationTaylor = False
notificationPolice = False
notificationDrDavies = False

Susan = False
Noah = False
Victoria = False
Taylor = False
Police = False
DrDavies = False


def photodeprofil():

	# Photo de profil Murphy
	screen.blit(pdpbase, (250,115))

	# Photo de profil destinataire
	screen.blit(pdpbase, (250,337))

	if DrDavies == True:
		screen.blit(pdpDrDavies, (250,337))


'''def affichermessages(l):
	screen.blit(l[x-4],(380,140))
	screen.blit(l[x-3],(380,170))
	screen.blit(l[x-2],(380,200))
	screen.blit(l[x-1],(380,230))
	screen.blit(l[x],(380,260))
	if bouton_flechehaut.draw() == True and not x==0:
		derniermessage-=1
	if bouton_flechebas.draw() == True and not x==(len(l)-1):
		derniermessage+=1'''


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



	'''

def messageriedef():
'''
