import pygame
pygame.init()

from textes import *

police = pygame.font.SysFont('Lucida' ,20)


PMurphy1_1 = police.render("Bonjour, je m'appelle Murphy Brown.",1,(100,100,100))
PMurphy1_2 = police.render("Je vous contacte avec urgence, mon fils a disparu depuis plus de 4h.",1,(100,100,100))
PMurphy1_3 = police.render("Nous l’avons cherché partout mais rien, nous avons besoin de votre aide.",1,(100,100,100))
PMurphy1_4 = police.render("Nous faitions son anniversaire.",1,(100,100,100))
PMurphy1_5 = police.render("Lorsque nous essayons de retrouver notre enfant pour qu’il ouvre ses cadeaux,",1,(100,100,100))
PMurphy1_6 = police.render("impossible de le retrouver dans toute la maison et personne n’a rien vu.",1,(100,100,100))
PMurphy1_7 = police.render("Nous avons commencé à chercher tout autour de la maison, mais toujours rien.",1,(100,100,100))
PMurphy1_8 = police.render("Faites vite s’il vous plaît. Nous sommes vraiment très inquiets",1,(100,100,100))
PMurphy1_9 = police.render("Cordialement.",1,(100,100,100))


Police2_1 = police.render("Bonjour Monsieur,",1,(100,100,100))
Police2_2 = police.render("Nous avons besoin du nom et prénom de votre enfant, de son âge et d’une photo de lui.",1,(100,100,100))
Police2_3 = police.render("Nous faisons tout pour accélérer nos recherches",1,(100,100,100))
Police2_4 = police.render("Cordialement",1,(100,100,100))

PMurphy3_1 = police.render("Il s’appelle Brown Marc et il n'a que 6 ans. ",1,(100,100,100))
PMurphy3_2 = police.render("Il fait une vingtaine de kilos et est blond aux yeux bleus",1,(100,100,100))

Police4_1 = police.render("Nous vous tiendrons au courant de la progression de notre enquête,",1,(100,100,100))
Police4_2 = police.render("Nous envisageons toutes les pistes et nous commençons",1,(100,100,100))
Police4_3 = police.render("par interroger les gens présents à cette fête.",1,(100,100,100))
Police4_4 = police.render("Nous cherchons aussi à savoir si l’un d’entre eux est mêlé à cette histoire.",1,(100,100,100))
Police4_5 = police.render("Bon courage Monsieur Brown.",1,(100,100,100))

PMurphy5_1 = police.render("Je suis certain que vous pouvez oublier cette piste, personne n'aurait pu",1,(100,100,100))
PMurphy5_2 = police.render("enlever notre enfant, il n'y avait que des amis proches de nous et de mon fils.",1,(100,100,100))

Police6_1 = police.render("Nous ne voulons écarter aucune piste.",1,(100,100,100))
Police6_2 = police.render("Le kidnappeur n'a laissé aucune trace, nous pouvons imaginer qu'il s'agit",1,(100,100,100))
Police6_3 = police.render("d'un récidiviste",1,(100,100,100))

PMurphy7_1 = police.render("Je vois...",1,(100,100,100))

conversationPolice = [nomMessagerieMurphy,PMurphy1_1,PMurphy1_2,PMurphy1_3,PMurphy1_4,PMurphy1_5,PMurphy1_6,PMurphy1_7,PMurphy1_8,PMurphy1_9,nomMessageriePolice,Police2_1,Police2_2,Police2_3,Police2_4,nomMessagerieMurphy,PMurphy3_1,PMurphy3_2,nomMessageriePolice,Police4_1,Police4_2,Police4_3,Police4_4,nomMessagerieMurphy,PMurphy5_1,PMurphy5_2,nomMessageriePolice,Police6_1,Police6_2,Police6_3,nomMessagerieMurphy,PMurphy7_1]