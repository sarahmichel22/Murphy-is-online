import pygame
pygame.init()

from textes import *

police = pygame.font.SysFont('Lucida' ,20)

DMurphy1_1 = police.render("Bonjour,",1,(100,100,100))
DMurphy1_2 = police.render("Je vous contacte car je suis tombé sur votre carte et j'aimerais savoir",1,(100,100,100))
DMurphy1_3 = police.render("si vous prenez toujours de nouveaux patients.",1,(100,100,100))
DMurphy1_4 = police.render("Cordialement,",1,(100,100,100))
DMurphy1_5 = police.render("Murphy Brown",1,(100,100,100))

Davies2_1 = police.render("Bonjour Monsieur Brown,",1,(100,100,100))
Davies2_2 = police.render("Je suis actuellement très prise par mes patients. Pouvez-vous m'expliquer",1,(100,100,100))
Davies2_3 = police.render("rapidement votre situation, nous fixerons une date ensemble.",1,(100,100,100))
Davies2_4 = police.render("Bien à vous,",1,(100,100,100))
Davies2_5 = police.render("Dr Davies",1,(100,100,100))

DMurphy3_1 = police.render("J'ai récemment subi un traumatisme suite à la perte de mon fils,",1,(100,100,100))
DMurphy3_2 = police.render("et je n'arrive pas à sortir la tête de l'eau. J'ai l'impression que je perds",1,(100,100,100))
DMurphy3_3 = police.render("le contrôle de ma vie et je ne sais plus quoi faire.",1,(100,100,100))

Davies4_1 = police.render("De ce que vous me dites, il vous faudrait un suivi au plus vite,",1,(100,100,100))
Davies4_2 = police.render("je vous propose de nous voir chaque mardi à 14h00 à partir de la semaine",1,(100,100,100))
Davies4_3 = police.render("prochaine.",1,(100,100,100))

DMurphy5_1 = police.render("Parfait je vous remercie.",1,(100,100,100))

DMurphy6_1 = police.render("Bonjour Dr.Davies,",1,(100,100,100))
DMurphy6_2 = police.render("Je rencontre de plus en plus de pertes de mémoire au cours de la journée.",1,(100,100,100))
DMurphy6_3 = police.render("Cela devient très handicapant au quotidien.",1,(100,100,100))
DMurphy6_4 = police.render("N'y aurait-il pas une alternative aux médicaments que vous me prescivez",1,(100,100,100))
DMurphy6_5 = police.render("actuellement?",1,(100,100,100))

Davies7_1 = police.render("Bonjour Monsieur Brown,",1,(100,100,100))
Davies7_2 = police.render("N'arrêtez surtout pas les médicaments d'un coup,",1,(100,100,100))
Davies7_3 = police.render("nous verrons tout cela ensemble ce mardi",1,(100,100,100))
Davies7_4 = police.render("Amicalement.",1,(100,100,100))

DMurphy8_1 = police.render("D'accord merci Docteur c'est parfait pour moi.",1,(100,100,100))

conversationDrDavies = [nomMessagerieMurphy, DMurphy1_1, DMurphy1_2, DMurphy1_3, DMurphy1_4, DMurphy1_5,nomMessagerieDrDavies, Davies2_1, Davies2_2, Davies2_3, Davies2_4, Davies2_5,nomMessagerieMurphy, DMurphy3_1, DMurphy3_2, DMurphy3_3, nomMessagerieDrDavies,Davies4_1,Davies4_2,Davies4_3,nomMessagerieMurphy,DMurphy5_1,nomMessagerieMurphy,DMurphy6_1,DMurphy6_2,DMurphy6_3,DMurphy6_4,DMurphy6_5,nomMessagerieDrDavies,Davies7_1,Davies7_2,Davies7_3,Davies7_4,nomMessagerieMurphy,DMurphy8_1]