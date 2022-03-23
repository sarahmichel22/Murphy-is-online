import pygame
pygame.init()

from textes import *

police = pygame.font.SysFont('Lucida' ,20)

TMurphy1_1 = police.render("Salut frérot, comment tu vas ?",1,(100,100,100))

Taylor2_1 = police.render("Bien bien, t'as besoin de quelque chose ?",1,(100,100,100))

TMurphy3_1 = police.render("Pourquoi tu penses que si je t'envoie un message c'est forcément parce",1,(100,100,100))
TMurphy3_2 = police.render("j'ai besoin de quelque chose ? ",1,(100,100,100))
TMurphy3_3 = police.render("Je peux très bien prendre des nouvelles de mon frère non ?",1,(100,100,100))

Taylor4_1 = police.render("Oui oui si tu le dis, bon comment tu vas ? ",1,(100,100,100))

TMurphy5_1 = police.render("Arrête de jouer les gros dûrs, je sais que tu es heureux que je ",1,(100,100,100))
TMurphy5_2 = police.render("prenne des nouvelles de toi :) ",1,(100,100,100))
TMurphy5_3 = police.render("Bah écoute tout va bien, on est en pleine préparation pour l'anniversaire",1,(100,100,100))
TMurphy5_4 = police.render("du petit. J'espère que son tonton sera présent !!",1,(100,100,100))

Taylor6_1 = police.render("Ahhh j'étais sûr que t'allais me demander un truc, bon je serai là haha",1,(100,100,100))

TMurphy7_1 = police.render("Parfait t'es le meilleur des tontons !",1,(100,100,100))

Taylor13_1 = police.render("Hey Murphy, viens chez moi !",1,(100,100,100))

TMurphy14_1 = police.render("D'accord je passerai ce soir.",1,(100,100,100))

TMurphy15_1 = police.render("T'es serieux pourquoi tu ne m'as pas préveue que Susan serait là.",1,(100,100,100))
TMurphy15_2 = police.render("Mais à quoi tu joues ?",1,(100,100,100))

Taylor16_1 = police.render("Elle est arrivée juste avant toi j'y peux rien, c'est pas ma faute.",1,(100,100,100))

TMurphy17_1 = police.render("J'espère vraiment que ce que tu dis est vrai.",1,(100,100,100))

Taylor18_1 = police.render("T'ES SERIEUX !!! Mais à quoi tu joues.",1,(100,100,100))
Taylor18_2 = police.render("T'as de la chance que Susan était la lorsque tu m'as annoncé que",1,(100,100,100))
Taylor18_3 = police.render("vous sortiez ensemble je sais pas ce que je t'aurais fait sinon.",1,(100,100,100))

TMurphy19_1 = police.render("Je t'en prie garde ton calme, c'était pas du tout voulu",1,(100,100,100))

Taylor20_1 = police.render("Tu te fous vraiment de moi, comment ça pas voulu ?",1,(100,100,100))
Taylor20_2 = police.render("Je veux rien savoir de toute façon, ne me parle plus jamais!",1,(100,100,100))

conversationTaylor = [nomMessagerieMurphy, TMurphy1_1, nomMessagerieTaylor, Taylor2_1, nomMessagerieMurphy, TMurphy3_1, TMurphy3_2, TMurphy3_3, nomMessagerieTaylor, Taylor4_1, nomMessagerieMurphy, TMurphy5_1, TMurphy5_2, TMurphy5_3, TMurphy5_4, nomMessagerieTaylor, Taylor6_1,nomMessagerieMurphy, TMurphy7_1, nomMessagerieTaylor, Taylor13_1, nomMessagerieMurphy, TMurphy14_1, nomMessagerieMurphy, TMurphy15_1, TMurphy15_2, nomMessagerieTaylor, Taylor16_1, nomMessagerieMurphy, TMurphy17_1, nomMessagerieTaylor, Taylor18_1, Taylor18_2, Taylor18_3, nomMessagerieMurphy, TMurphy19_1, nomMessagerieTaylor, Taylor20_1, Taylor20_2]