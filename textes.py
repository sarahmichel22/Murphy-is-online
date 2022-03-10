import pygame
pygame.init()
from menu import *
from telechargement_images import *
from classes import *

police = pygame.font.Font('LLPIXEL3.ttf' ,20)

#paramètres
volumemusique = police.render("Volume de la musique : ", 1, (100,100,100))
volumeson = police.render("Volume du son : ",1,(100,100,100))
changerpdp = police.render("Changer la photo de profil",1,(46, 175, 240))
traitbas = police.render("______________________",1,(100,100,100))

titrenavigateur = police.render( "Navigateur", 1 , (255,255,255) )
titredossier = police.render( "Galerie", 1 , (255,255,255) )
titremessagerie = police.render( "Messagerie", 1 , (255,255,255) )
titrenotes = police.render( "Notes", 1 , (255,255,255) )
titreparametres = police.render( "Paramètres", 1 , (255,255,255) )

police = pygame.font.SysFont('Lucida' ,20)

titreimage1 = police.render("Soirée du nouvel an chez Noah",1, (100,100,100))
titreimage2 = police.render("Promenade au parc avec Sumo",1, (100,100,100))
titreimage3 = police.render("Atelier cuisine de mon petit Marc",1, (100,100,100))
titreimage4 = police.render("Journée pique-nique avec Marc et Victoria",1, (100,100,100))
titreimage5 = police.render("Mon premier rendez-vous avec Susan",1, (100,100,100))
titreimage6 = police.render("Concert de Metallica à Paris",1, (100,100,100))
titreimage7 = police.render("Soirée privée du groupe Arctic Monkeys",1, (100,100,100))
titresimages = [titreimage1,titreimage2,titreimage3,titreimage4,titreimage5,titreimage6,titreimage7]

#police = pygame.font.Font('cream-DEMO.ttf',15)
police = pygame.font.SysFont('Lucida' ,20)

titreonglet1 = police.render("xanax                                  ", 1, (100,100,100))
titreonglet2 = police.render("perte de memoire                                   ", 1, (100,100,100))
titrerecherche1 = police.render("https://www.search.com/search=xanax", 1, (100,100,100))
titrerecherche2 = police.render("https://attentionauxanxiolytiques.com/", 1, (100,100,100))

#Notes
police = pygame.font.Font('LLPIXEL3.ttf' ,20)
mdpnotes = police.render("Veuillez entrer le mot de passe :",1,(100,100,100))


police = pygame.font.Font('LLPIXEL3.ttf' ,30)

traitnombre = police.render("___",1,(100,100,100))

zero2 = police.render("0",0,(100,100,100))
un2 = police.render("___",1,(100,100,100))
deux2 = police.render("___",2,(100,100,100))
trois2 = police.render("___",3,(100,100,100))
quatre2 = police.render("___",4,(100,100,100))
cinq2 = police.render("___",5,(100,100,100))
six2 = police.render("___",6,(100,100,100))
sept2 = police.render("___",7,(100,100,100))
huit2 = police.render("___",8,(100,100,100))
neuf2 = police.render("___",9,(100,100,100))

police = pygame.font.SysFont('Lucida' ,20)

#Nom de contacts
nomMurphy = police.render("Murphy",0,(100,100,100))
nomSusan = police.render("Susan",0,(100,100,100))
nomNoah = police.render("Noah",0,(100,100,100))
nomVictoria = police.render("Victoria",0,(100,100,100))
nomTaylor = police.render("Taylor",0,(100,100,100))
nomPolice = police.render("Police",0,(100,100,100))
nomDrDavies = police.render("Dr Davies",0,(100,100,100))

#nom contact messagerie
police = pygame.font.SysFont('Lucida' ,22)

nomMessagerieMurphy = police.render("Murphy :",0,(110,160,220))
nomMessagerieSusan = police.render("Susan :",0,(249,58,58))
nomMessagerieNoah = police.render("Noah :",0,(249,58,58))
nomMessagerieVictoria = police.render("Victoria :",0,(249,58,58))
nomMessagerieTaylor = police.render("Taylor :",0,(249,58,58))
nomMessageriePolice = police.render("Police :",0,(249,58,58))
nomMessagerieDrDavies = police.render("Dr Davies :",0,(249,58,58))