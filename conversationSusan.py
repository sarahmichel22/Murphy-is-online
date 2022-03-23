from email import message
import pygame
pygame.init()

from textes import *

police = pygame.font.SysFont('Lucida' ,20)

Susan0_1 = police.render("Salut chéri, Noah m'a prévenue qu'il avait réussi",1,(100,100,100))
Susan0_2 = police.render("à avoir deux places pour le concert d'Arctic Monkeys à Paris.  ",1,(100,100,100))
Susan0_3 = police.render("Il m'a demandé si tu pouvais y aller avec lui et j'ai répondu ",1,(100,100,100))
Susan0_4 = police.render("oui sans hésiter, je sais que c'est ton groupe préféré, ",1,(100,100,100))
Susan0_5 = police.render("alors vas-y et profite à fonnnnd !!!",1,(100,100,100))
Susan0_6 = police.render("",1,(100,100,100))


######################################################

Susan1 = police.render("Coucou mon coeur comment tu vas ?",1,(100,100,100))
messageSusan1 = [Susan1]

######################################################

SMurphy2_1 = police.render("Salut, je vais très bien et toi ?",1,(100,100,100))
SMurphy2_2 = police.render("Ca ne va pas trop bien, je suis fatigué",1,(100,100,100))
SMurphy2_3 = police.render("Je suis désolé mais je crois que vous faites erreur sur la personne",1,(100,100,100))
messageMurphy2_1 = SMurphy2_1
messageMurphy2_2 = SMurphy2_2
messageMurphy2_3 = SMurphy2_3
messageSMurphy2 = [messageMurphy2_1, messageMurphy2_2, messageMurphy2_3]

########################################################


Susan3_1_1 = police.render("Tant mieux ça veut dire que tes médicaments font surement effet, bonne nouvelle! ",1,(100,100,100))
Susan3_1_2 = police.render("Je vais bien aussi, le trajet été un peu long mais je suis heureuse de retrouver",1,(100,100,100))
Susan3_1_3 = police.render("ma famille, ils m'avaient manqué",1,(100,100,100))
Susan3_2 = police.render("Tu devrais te reposer alors si tu es fatigué, c'est surement tes médicaments qui ",1,(100,100,100))
Susan3_2_1 = police.render("font effet ! De mon côté je suis bien arrivée chez ma famille.",1,(100,100,100))
Susan3_3_1 = police.render("Je suis avec ma famille je ne peux pas gérer tes problèmes de mémoire",1,(100,100,100))
Susan3_3_2 = police.render("mais pour commencer est-ce que tu as bien pris tes médicaments ?",1,(100,100,100))
messageSusan3_1 = [Susan3_1_1,Susan3_1_2, Susan3_1_3]
messageSusan3_2 = [Susan3_2,Susan3_2_1]
messageSusan3_3 = [Susan3_3_1,Susan3_3_2]
messageSusan3 = [messageSusan3_1,messageSusan3_2,messageSusan3_3]

########################################################

SMurphy4_1 = police.render("Ah tu es avec ta famille, vous avez prévu de faire quelque chose en particulier ?",1,(100,100,100))
SMurphy4_2 = police.render("Excuse-moi, j'aimerais vraiment savoir qui tu es ?",1,(100,100,100))
SMurphy4_3 = police.render("Quels médicaments ?",1,(100,100,100))
messageSMurphy4 = [SMurphy4_1,SMurphy4_2,SMurphy4_3]

########################################################

Susan5_1_1 = police.render("Oui je t'avais prévenu que j'allais les voir ce week-end. Pour le moment on va ",1,(100,100,100))
Susan5_1_2 = police.render("manger au restaurant, après je pense que l'on va faire des sorties durant la semaine.",1,(100,100,100))
Susan5_1_3 = police.render("Mais je vais aussi essayer de me reposer. Tu devrais en faire autant, Je t'en",1,(100,100,100))
Susan5_1_4 = police.render("parlerai plus en détail quand j'aurai plus de temps je dois y aller! Bisous",1,(100,100,100))
#Hors ligne
Susan5_2_1 = police.render("Mince !! Pourtant j'avais prévenue Taylor qu'il devait t'aider durant mon",1,(100,100,100))
Susan5_2_2 = police.render("absence en te donnant justement tes médicaments.",1,(100,100,100))
Susan5_2_3 = police.render("Ne bouge pas je lui envoie un message !!",1,(100,100,100))
Susan5_3 = police.render("Les médicaments que la psychiatre t'a prescrit.",1,(100,100,100))
messageSusanh5_1=[Susan5_1_1,Susan5_1_2,Susan5_1_3, Susan5_1_4]
messageSusan5_2=[Susan5_2_1,Susan5_2_2,Susan5_2_3]
messageSusan5_3=[Susan5_3,Susan5_2_1,Susan5_2_2,Susan5_2_3]
messageSusan5 = [messageSusanh5_1,messageSusan5_2,messageSusan5_3]

########################################################

SMurphy6_1 = police.render("Mais ces médicaments sont vraiment bons pour moi ? ",1,(100,100,100))
SMurphy6_2 = police.render("Tu peux m'expliquer la situation ? Je n'y comprends plus rien",1,(100,100,100))
SMurphy6_3 = police.render("Qui est Taylor ?",1,(100,100,100))
messageSMurphy6 = [SMurphy6_1,SMurphy6_2,SMurphy6_3]

########################################################

Susan7_1_1 = police.render("Je ne m'y connais pas, mais la psychiatre a insisté pour que tu prennes cela.",1,(100,100,100))

Susan7_2_1 = police.render("Je ne suis même pas certaine que tu sois en état de comprendre ce que je vais",1,(100,100,100))
Susan7_2_2 = police.render("te dire, mais actuellement tu dois prendre des médicaments et j'avais justement ",1,(100,100,100))
Susan7_2_3 = police.render("demandé à Taylor de t'aider.",1,(100,100,100))

Susan7_3_1 = police.render("Ca devient vraiment grave...",1,(100,100,100))
Susan7_3_2 = police.render("Taylor est ton frère, même si parfois il ne se comporte pas comme tel.",1,(100,100,100))

messageSusan7_1 = [Susan7_1_1]
messageSusan7_2 = [Susan7_2_1,Susan7_2_2,Susan7_2_3]
messageSusan7_3 = [Susan7_3_1,Susan7_3_2]
messageSusan7 = [messageSusan7_1,messageSusan7_2,messageSusan7_3]

########################################################

SMurphy8_1 = police.render("Tu penses que je devrais me méfier de Taylor ?",1,(100,100,100))
SMurphy8_2 = police.render("Tu penses que je devrais me méfier du Dr.Davies ?",1,(100,100,100))
SMurphy8_3 = police.render("Qu'est ce que je dois faire maintenant ?",1,(100,100,100))
messageSMurphy8 = [SMurphy8_1,SMurphy8_2,SMurphy8_3]

########################################################

Susan9_1_1 = police.render("Ta question est étrange je ne sais pas pourquoi tu te demandes ça. C'est ton frère",1,(100,100,100))
Susan9_1_2 = police.render("quand même! Sa jalousie prend parfois le dessus mais il n'est pas méchant.",1,(100,100,100))


Susan9_2_1 = police.render("Je ne sais pas quoi te dire d'elle, c'est une psychiatre professionnelle et gentille",1,(100,100,100))
Susan9_2_2 = police.render("même parfois un peu trop amicale. Il est vrai que les médicaments qu'elle te ",1,(100,100,100))
Susan9_2_3 = police.render("prescrit ont pas mal d'effets secondaires sur toi.",1,(100,100,100))

Susan9_3_1 = police.render("Tu devrais commencer par te reposer, je vais essayer d'arranger ça.",1,(100,100,100))

Susanfin = police.render("Bon j'ai réussi à joindre Taylor ça devrait aller maintenant, fais attention à toi !",1,(100,100,100))
#Hors ligne

messageSusan9_1 = [Susan9_1_1,Susan9_1_2,Susanfin]
messageSusan9_2 = [Susan9_2_1,Susan9_2_2,Susan9_2_3,Susanfin]
messageSusan9_3 = [Susan9_3_1,Susanfin]
messageSusan9 = [messageSusan9_1,messageSusan9_1,messageSusan9_1]

conversationSusan = [nomMessagerieSusan,Susan0_1,Susan0_2,Susan0_3,Susan0_4,Susan0_5]