import pygame
pygame.init()

from textes import *

police = pygame.font.SysFont('Lucida' ,20)

Noah1 = police.render("Hey Murphy !",1,(100,100,100))
messageNoah1 = [Noah1]

######################################################

NMurphy2_1 = police.render("Salut !",1,(100,100,100))
NMurphy2_2 = police.render("Comment tu vas ?",1,(100,100,100))
NMurphy2_3 = police.render("Qui es-tu ?",1,(100,100,100))
messageNMurphy2_1 = [NMurphy2_1]
messageNMurphy2_2 = [NMurphy2_2]
messageNMurphy2_3 = [NMurphy2_3]
messageNMurphy2 = [messageNMurphy2_1,messageNMurphy2_2,messageNMurphy2_3]

#######################################################

Noah3_1 = police.render("Comment tu vas depuis le temps ?",1,(100,100,100))
Noah3_2 = police.render("Ca va super bien, j'ai plein de choses à te raconter ! et toi ?",1,(100,100,100))
Noah3_3 = police.render("T'es sûr que tu vas bien ? Tu te rapelles plus de ton meilleur ami ?",1,(100,100,100))
messageNoah3_1 = [Noah3_1]
messageNoah3_2 = [Noah3_2]
messageNoah3_3 = [Noah3_3]
messageNoah3 = [messageNoah3_1,messageNoah3_2,messageNoah3_3]

#######################################################

NMurphy4_1 = police.render("Je vais bien !",1,(100,100,100))
NMurphy4_2 = police.render("Ca ne va pas super bien.",1,(100,100,100))
NMurphy4_3 = police.render("Je préfère ne pas en parler.",1,(100,100,100))
messageNMurphy4_1 = [NMurphy4_1]
messageNMurphy4_2 = [NMurphy4_2]
messageNMurphy4_3 = [NMurphy4_3]
messageNMurphy4 = [messageNMurphy4_1,messageNMurphy4_2,messageNMurphy4_3]

########################################################

NMurphy7_2 = police.render("Super, raconte moi tout !",1,(100,100,100))
NMurphy8_2 = NMurphy4_1
NMurphy9_2 = police.render("J'ai pas l'habide de raconter des choses à un inconnu.",1,(100,100,100))

conversationNMurphy3 = [NMurphy7_2, NMurphy8_2, NMurphy9_2]

Noah4 = police.render("T'as toujours été réservé de toute façon, et le passé n'a pas aidé.",1,(100,100,100))
Noah4_1 = police.render("Bon j'ai trop de chose à te raconter",1,(100,100,100))
Noah5 = police.render("Tu sais que tu peux tout me raconter ! je suis ton meilleur ami.",1,(100,100,100))
Noah5_1 = police.render("C'est encore cette histoire avec ton enfant ?",1,(100,100,100))
Noah6 = Noah5
Noah6_1 = Noah5_1

NMurphy10_3 = police.render("Mon meilleur ami ?",1,(100,100,100))
NMurphy11_3 = police.render("C'était une blague, tu crois que j'aurai oublie mon meilleur ami.",1,(100,100,100))
NMurphy12_3 = NMurphy4_1

conversationNMurphy4 = [NMurphy10_3, NMurphy11_3, NMurphy12_3]



Noah7 = police.render("Mec j'ai été accepté pour mon travail et Laura m'a accordé un rencart !",1,(100,100,100))
Noah8 = Noah4
Noah8_1 = Noah4_1
Noah9 = police.render("Tu m'inquiètes vraiment, t'as encore tes pertes de mémoire ?",1,(100,100,100))

Noah10 = Noah9
Noah11 = police.render("AHAHA ! Tu m'as fait peur, bon je dois te raconter des choses !!",1,(100,100,100))
Noah12 = Noah4
Noah12_1 = Noah4_1

NMurphy13_4 = NMurphy7_2
NMurphy14_4 = police.render("C'est naturel d'être réservé avec un inconnu",1,(100,100,100))
NMurphy15_4 = police.render("Tu me connais mieux que personne, il s'est passé quoi durant le passé ?",1,(100,100,100))


conversationNMurphy2 = [NMurphy13_4, NMurphy14_4, NMurphy15_4]

NMurphy16_5 = police.render("De quelle histoire tu parles ?",1,(100,100,100))
NMurphy17_5 = police.render("Je peux vraiment tout te dire? est ce que tu peux m'en parler de cette histoire",1,(100,100,100))
NMurphy18_5 = police.render("Oui c'est ça, c'est un peu compliqué...",1,(100,100,100))
NMurphy18_5_1 = police.render("mais bon je vais bientôt voir Arctic Monkeys ça va me changer les idée !!",1,(100,100,100))

conversationNMurphy2 = [NMurphy16_5, NMurphy17_5, NMurphy18_5]

NMurphy19_6 = NMurphy16_5
NMurphy20_6 = NMurphy17_5
NMurphy21_6 = NMurphy18_5
NMurphy21_6_1 = NMurphy18_5_1

conversationNMurphy2 = [NMurphy16_5, NMurphy17_5, NMurphy18_5]

NMurphy22_7 = police.render("C'est quoi comme travail?",1,(100,100,100))
NMurphy23_7 = police.render("Laura, je la connais?",1,(100,100,100))
NMurphy24_7 = police.render("T'es trop chanceux, tu comptes organiser quoi pour le date?",1,(100,100,100))

conversationNMurphy2 = [NMurphy22_7, NMurphy23_7, NMurphy24_7]

NMurphy25_8 = NMurphy13_4
NMurphy26_8 = NMurphy14_4
NMurphy27_8 = NMurphy15_4

conversationNMurphy2 = [NMurphy25_8, NMurphy26_8, NMurphy27_8]

NMurphy28_9 = police.render("De quelle perte de mémoire tu parles?",1,(100,100,100))
NMurphy29_9 = police.render("C'est sûrement mes médicament",1,(100,100,100))
NMurphy30_9 = police.render("je ne serai te répondre, tu peux m'en dire plus?",1,(100,100,100))

conversationNMurphy2 = [NMurphy28_9, NMurphy29_9, NMurphy30_9]

NMurphy31_10 = NMurphy28_9
NMurphy32_10 = NMurphy29_9
NMurphy33_10 = NMurphy30_9

conversationNMurphy2 = [NMurphy31_10, NMurphy32_10, NMurphy33_10]

NMurphy34_11 = police.render("Une prochaine fois je dois prendre des billet pour Arctic Monkeys.",1,(100,100,100))
NMurphy35_11 = NMurphy7_2
NMurphy36_11 = police.render("il ne faut pas t'en porter autant pour une blague !!",1,(100,100,100))

conversationNMurphy2 = [NMurphy34_11, NMurphy35_11, NMurphy36_11]


NMurphy37_12 = NMurphy13_4
NMurphy38_12 = NMurphy14_4
NMurphy39_12 = NMurphy15_4

conversationNMurphy2 = [NMurphy37_12, NMurphy38_12, NMurphy39_12]

Noah13 = Noah7
Noah14 = police.render("Je te trouve vraiment bizarre, qu'est ce qu'il t'arrive",1,(100,100,100))
Noah14_1 = police.render("tu m'inquiètes j'envoie un message à Susan",1,(100,100,100))
Noah15 = police.render("Bien sûr! On se connaît depuis des années !!",1,(100,100,100))
Noah15_1 = police.render("Par où commencer, tu sais bien qu'après la disparition de ton fils,",1,(100,100,100))
Noah15_2 = police.render("tu ne savais plus quoi faire et tu as commencé à délirer. ",1,(100,100,100))
Noah15_3 = police.render("On a dû te trouver un psychiatre pour t'aider à oublier ton fils. ",1,(100,100,100))

Noah16 = Noah14
Noah16_1 = Noah14_1
Noah17 = Noah15
Noah17_1 = Noah15_1
Noah17_2 = Noah15_2
Noah17_3 = Noah15_3

Noah18 = police.render("TROP COOL, profite bien je sais à quel point tu adores ce groupe !!",1,(100,100,100))
Noah19 = Noah14
Noah19_1 = Noah14_1
Noah20 = Noah15
Noah20_1 = Noah15_1
Noah20_2 = Noah15_2
Noah20_3 = Noah15_3

Noah21 = Noah18
Noah22 = police.render("Le travail pour lequel nous avons suivie les mêmes études «informaticien»",1,(100,100,100))
Noah23 = police.render("t'as vraiment oublier la seule fille dont je te parle tout le temps",1,(100,100,100))
Noah24 = police.render("En fait, je vais pas te mentir, je voulais faire un rdv à 4: toi, Susan et moi, Laura",1,(100,100,100))


Noah25 = Noah7
Noah26 = Noah14
Noah26_1 = Noah14_1

Noah27 = Noah15
Noah27_1 = Noah15_1
Noah27_2 = Noah15_2
Noah27_2 = Noah15_3 

Noah28 = Noah14
Noah28_1 = Noah14_1
Noah29 = police.render("Oui c'est surement ça, tu devrais te reposer. je te laisse bise",1,(100,100,100))
Noah30 = Noah15_1
Noah30_1 = Noah15_2
Noah30_2 = Noah15_3
Noah31 = Noah14
Noah31_1 = Noah14_1
Noah32 = Noah29
Noah33 = Noah15_1
Noah33_1 = Noah15_2
Noah33_2 = Noah15_3

Noah34 = police.render("Bon ok une prochaine fois profites bien de ton groupe préféré !!",1,(100,100,100))
Noah35 = Noah7
Noah36 = police.render("Tu peux pas m'en vouloir, j'ai encore cru que tes problèmes de mémoire étaient revenu!",1,(100,100,100))
Noah37 = Noah7
Noah38 = Noah14
Noah38_1 = Noah14_1
Noah39 = Noah15
Noah39_1 = Noah15_1
Noah39_2 = Noah15_2
Noah39_3 = Noah15_3

NMurphy40_15 = police.render("Merci de m'avoir tout raconter, je vais devoir te laisser.",1,(100,100,100))
NMurphy40_17 = NMurphy40_15
NMurphy40_20 = NMurphy40_15
NMurphy40_27 = NMurphy40_15
NMurphy40_30 = NMurphy40_15
NMurphy40_33 = NMurphy40_15
NMurphy40_39 = NMurphy40_15

NMurphy40_18 = police.render("Merci je te raconterai",1,(100,100,100))
NMurphy40_21 = NMurphy40_18

NMurphy40_22 = police.render("Je suis désolé, je vais te laisser on en parle un prochaine fois",1,(100,100,100))
NMurphy40_23 = NMurphy40_22 
NMurphy40_24 = NMurphy40_22 

NMurphy40_36 = police.render("Non t'en fais pas se n'est pas le cas mais bon je vais me reposer",1,(100,100,100))





conversationNoah = []