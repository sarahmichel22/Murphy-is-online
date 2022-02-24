import pygame
pygame.init()
from menu import *
from telechargement_images import *
from classes import *

police = pygame.font.Font('LLPIXEL3.ttf' ,20)

titrenavigateur = police.render( "Navigateur", 1 , (255,255,255) )
titredossier = police.render( "Galerie", 1 , (255,255,255) )
titremessagerie = police.render( "Messagerie", 1 , (255,255,255) )
titrenotes = police.render( "Notes", 1 , (255,255,255) )
titreparametres = police.render( "Paramètres", 1 , (255,255,255) )

police = pygame.font.SysFont('Lucida' ,20)

titreimage1 = police.render("Soirée du nouvel an chez Noah",1, (200, 200, 200))
titreimage2 = police.render("Promenade au parc avec Sumo",1, (200, 200, 200))
titreimage3 = police.render("Atelier cuisine de mon petit Marc",1, (200, 200, 200))
titreimage4 = police.render("Journée pique-nique avec Marc et Victoria",1, (200, 200, 200))
titreimage5 = police.render("Mon premier rendez-vous avec Susan",1, (200, 200, 200))
titreimage6 = police.render("Concert de Metallica à Paris",1, (200, 200, 200))
titreimage7 = police.render("Soirée privée du groupe Arctic Monkeys",1, (200, 200, 200))
titresimages = [titreimage1,titreimage2,titreimage3,titreimage4,titreimage5,titreimage6,titreimage7]

#police = pygame.font.Font('cream-DEMO.ttf',15)
police = pygame.font.SysFont('Lucida' ,20)

titreonglet1 = police.render("xanax                                  ", 1, (100,100,100))
titreonglet2 = police.render("perte de memoire                                   ", 1, (100,100,100))
titrerecherche1 = police.render("https://www.search.com/search=xanax", 1, (100,100,100))
titrerecherche2 = police.render("https://attentionauxanxiolytiques.com/", 1, (100,100,100))