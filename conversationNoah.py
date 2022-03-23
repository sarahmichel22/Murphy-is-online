import pygame
pygame.init()

from textes import *

police = pygame.font.SysFont('Lucida' ,20)

Noah0_1 = police.render("Hé mec, devine ce que j'ai choppé!",1,(100,100,100))
Noah0_2 = police.render("Deux places pour le concert d'Arctic Monkeys à Paris!",1,(100,100,100))
Noah0_3 = police.render("Le 19 novembre, prépare-toi!!",1,(100,100,100))
Noah0_4 = police.render("Et interdiction de te désister, je sais que ça te ferra du bien.",1,(100,100,100))
Noah0_5 = police.render("J'ai déjà hâte!",1,(100,100,100))

######################################################

Noah1 = police.render("Hey Murphy ! Comment tu vas?",1,(100,100,100))
messageNoah1 = [Noah1]

######################################################

NMurphy2_1 = police.render("Je vais bien !",1,(100,100,100))
NMurphy2_2 = police.render("Ca ne va pas super bien.",1,(100,100,100))
NMurphy2_3 = police.render("Qui êtes-vous?",1,(100,100,100))
messageNMurphy2_1 = NMurphy2_1
messageNMurphy2_2 = NMurphy2_2
messageNMurphy2_3 = NMurphy2_3
messageNMurphy2 = [messageNMurphy2_1,messageNMurphy2_2,messageNMurphy2_3]

########################################################


Noah3_1_1 = police.render("Tant mieux! Ca fait plaisir à lire.",1,(100,100,100))
Noah3_1_2 = police.render("Bon j'ai plein de choses à te raconter!",1,(100,100,100))
Noah3_2 = police.render("Haha, très drôle.",1,(100,100,100))
Noah3_3_1 = police.render("C'est encore cette histoire avec ton enfant j'imagine...",1,(100,100,100))
Noah3_3_2 = police.render("Je ne vais pas insisté ça risquerait de te faire de la peine.",1,(100,100,100))
messageNoah3_1 = [Noah3_1_1,Noah3_1_2]
messageNoah3_3 = [Noah3_2,Noah3_1_2]
messageNoah3_2 = [Noah3_3_1,Noah3_3_2,Noah3_1_2]
messageNoah3 = [messageNoah3_1,messageNoah3_2,messageNoah3_3]

########################################################

NMurphy4_1 = police.render("Super, raconte moi tout !",1,(100,100,100))
NMurphy4_2 = police.render("Excuse-moi, j'aimerais vraiment savoir qui tu es",1,(100,100,100))
NMurphy4_3 = police.render("Qui est <<Arctic Monkeys>> ?",1,(100,100,100))
messageNMurphy4 = [NMurphy4_1,NMurphy4_2,NMurphy4_3]

########################################################

Noah5_1_1 = police.render("J'ai été accepté pour le job dont je t'ai parlé la dernière fois!",1,(100,100,100))
Noah5_1_2 = police.render("Mes collègues sont super sympa et je me sens vraiment bien dans l'équipe",1,(100,100,100))
Noah5_1_3 = police.render("Bon! Je t'en parlerai plus en détail une prochaine fois je dois y aller!",1,(100,100,100))
#Hors ligne
Noah5_2_1 = police.render("Tu m'inquiètes vraiment, t'as encore tes pertes de mémoire ?",1,(100,100,100))
Noah5_2_2 = police.render("Ton état s'est vraiment empiré ces derniers temps, tu es sûr que les",1,(100,100,100))
Noah5_2_3 = police.render("médicaments que tu prends améliorent vraiment ta santé mentale?",1,(100,100,100))
Noah5_2_4 = police.render("Fais attention à toi en tout cas...",1,(100,100,100))
Noah5_3 = police.render("C'est ton groupe préféré! On les as vus en concert plein de fois ensemble!",1,(100,100,100))
messageNoah5_1=[Noah5_1_1,Noah5_1_2,Noah5_1_3]
messageNoah5_2=[Noah5_2_1,Noah5_2_2,Noah5_2_3,Noah5_2_4]
messageNoah5_3=[Noah5_3,Noah5_2_1,Noah5_2_2,Noah5_2_3,Noah5_2_4]
messageNoah5 = [messageNoah5_1,messageNoah5_2,messageNoah5_3]

########################################################

NMurphy6_1 = police.render("Je plaisante avec toi, tu penses que je pourrais t'oublier?",1,(100,100,100))
NMurphy6_2 = police.render("Peux-tu me parler plus en détail de la situation?",1,(100,100,100))
NMurphy6_3 = police.render("Pouvez-vous me dire qui sont toutes ces personnes sur ma messagerie?",1,(100,100,100))
messageNMurphy6 = [NMurphy6_1,NMurphy6_2,NMurphy6_3]

########################################################

Noah7_1_1 = police.render("Ouf, tu m'as vraiment fait peur pour le coup!",1,(100,100,100))
Noah7_1_2 = police.render("Du coup revenons-en à ce que j'avais l'intention de te raconter",1,(100,100,100))
#Hors ligne
Noah7_2_1 = police.render("C'est un peu délicat de parler de ça par message...",1,(100,100,100))
Noah7_2_2 = police.render("J'imagine que tu devrais en parler à Susan, elle est plus douée que moi",1,(100,100,100))
Noah7_2_3 = police.render("pour ce genre de chose, je lui passe un coup de fil.",1,(100,100,100))
Noah7_2_4 = police.render("Quant à moi je vais te laisser, si tu as besoin de quoi que ce soit tu ",1,(100,100,100))
Noah7_2_5 = police.render("peux compter sur moi!",1,(100,100,100))
#Hors ligne
Noah7_3_1 = police.render("C'est donc critique à ce point...",1,(100,100,100))
Noah7_3_2 = police.render("Ecoute, pour être honnête avec toi je ne sais pas si je suis la personne",1,(100,100,100))
Noah7_3_3 = police.render("la plus douée pour gérer tes pertes de mémoire et ta santé mentale, si tu",1,(100,100,100))
Noah7_3_4 = police.render("veux mon avis, parles-en à un professionnel.",1,(100,100,100))
Noah7_3_5 = police.render("Et passe du temps avec ta copine Susan, ça vous fera du bien.",1,(100,100,100))
messageNoah7_1 = [Noah7_1_1,Noah7_1_2,Noah5_1_1,Noah5_1_2,Noah5_1_3]
messageNoah7_2 = [Noah7_2_1,Noah7_2_2,Noah7_2_3,Noah7_2_4,Noah7_2_5]
messageNoah7_3 = [Noah7_3_1,Noah7_3_2,Noah7_3_3,Noah7_3_4]
messageNoah7 = [messageNoah7_1,messageNoah7_2,messageNoah7_3]

########################################################

NMurphy8_1 = police.render("Tu penses que je devrais me méfier de Taylor?",1,(100,100,100))
NMurphy8_2 = police.render("Tu penses que je devrais me méfier du Dr Davies?",1,(100,100,100))
NMurphy8_3 = police.render("Tu penses que je devrais me méfier de Susan?",1,(100,100,100))
messageNMurphy8 = [NMurphy8_1,NMurphy8_2,NMurphy8_3]

########################################################

Noah9_1_1 = police.render("Tu me mets mal à l'aise avec cette question, c'est ton frère après tout",1,(100,100,100))
Noah9_1_2 = police.render("je peux pas réellement me permettre de donner mon avis sur lui.",1,(100,100,100))
Noah9_1_3 = police.render("Je peux simplement dire qu'il n'a pas l'air très net et certainement",1,(100,100,100))
Noah9_1_4 = police.render("pas quelqu'un en qui tu devrais accorder ta confiance. Fais attention",1,(100,100,100))
Noah9_1_5 = police.render("à lui, il t'a toujours énormément jalousé.",1,(100,100,100))

Noah9_2_1 = police.render("Difficile à dire, elle est très professionnelle et ne semble rien dégager",1,(100,100,100))
Noah9_2_2 = police.render("de mauvais mais ton état ne s'est pas amélioré depuis que tu vas consulter",1,(100,100,100))
Noah9_2_3 = police.render("chez elle, je doute surtout de ses capacités.",1,(100,100,100))

Noah9_3_1 = police.render("Tu as perdu la tête ma parole! S'il y a bien une personne en qui tu peux",1,(100,100,100))
Noah9_3_2 = police.render("te confier librement c'est elle.",1,(100,100,100))
Noah9_3_3 = police.render("Même si elle n'était pas malheureuse de votre rupture, Victoria et toi,",1,(100,100,100))
Noah9_3_4 = police.render("je ne pense pas qu'elle soit mauvaise. Rappelle-toi qu'elle a été là",1,(100,100,100))
Noah9_3_5 = police.render("pour toi quand ça n'allait pas, et c'est le plus important.",1,(100,100,100))

Noahfin = police.render("Sur ce je te laisse! Fais attention à toi et appelle moi si tu as besoin!",1,(100,100,100))
#Hors ligne

messageNoah9_1 = [Noah9_1_1,Noah9_1_2,Noah9_1_3,Noah9_1_4,Noah9_1_5,Noahfin]
messageNoah9_2 = [Noah9_2_1,Noah9_2_2,Noah9_2_3,Noahfin]
messageNoah9_3 = [Noah9_3_1,Noah9_3_2,Noah9_3_3,Noah9_3_4,Noah9_3_5,Noahfin]
messageNoah9 = [messageNoah9_1,messageNoah9_2,messageNoah9_3]




conversationNoah = [nomMessagerieNoah,Noah0_1,Noah0_2,Noah0_3,Noah0_4,Noah0_5]