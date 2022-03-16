import pygame
pygame.init()

from textes import *

police = pygame.font.SysFont('Lucida' ,20)

Victoria1_1 = police.render("Je rentrerai tard ce soir. S'il te plaît, fais prendre la douche à Marc et mets",1, (100,100,100))
Victoria1_2 = police.render("le au lit avant que j’arrive. N’oublie pas de lui raconter sa petite histoire.",1,(100,100,100))

VMurphy2_1 = police.render("Oui bien sûr ma chérie je m'en occupe, fais attention à toi.",1, (100,100,100))

Victoria3_1 = police.render("Bonjour mon coeur, pourras-tu t'occuper d'envoyer les invitations pour",1, (100,100,100))
Victoria3_2 = police.render("l'anniversaire de Marc?",1, (100,100,100))

VMurphy4_1 = police.render("Oui bien sûr!",1, (100,100,100))

Victoria5_1 = police.render("Tu rentres encore tard ce soir ? Rejoins-moi, on va traverser ça ensemble", 1,(100,100,100))

Victoria6_1 = police.render("Bonjour, j’ai pris rendez-vous avec l’avocat.", 1,(100,100,100))
Victoria6_2 = police.render("Nous devons nous présenter devant lui, le 09/06.", 1,(100,100,100))

VMurphy7_1 = police.render("Sommes-nous vraiment obligés d’en arriver là ?", 1,(100,100,100))

Victoria8_1 = police.render("Il fallait y penser le soir ou je t’ai demandé ", 1,(100,100,100))
Victoria8_2 = police.render("de me rejoindre parce que j’avais besoin que tu sois à mes côtés.", 1,(100,100,100))

VMurphy9_1 = police.render("Tu as raison et je te demande pardon, j’ai perdu contrôle.", 1,(100,100,100))

Victoria10_1 = police.render("Nous nous reverrons le 09/06. Au revoir Murphy !", 1,(100,100,100))

conversationVictoria = [nomMessagerieVictoria,Victoria1_1,Victoria1_2,nomMessagerieMurphy,VMurphy2_1,nomMessagerieVictoria,Victoria3_1,Victoria3_2,nomMessagerieMurphy,VMurphy4_1,nomMessagerieVictoria,Victoria5_1,nomMessagerieVictoria,Victoria6_1,Victoria6_2,nomMessagerieMurphy,VMurphy7_1,nomMessagerieVictoria,Victoria8_1,Victoria8_2,nomMessagerieMurphy,VMurphy9_1,nomMessagerieVictoria,Victoria10_1]