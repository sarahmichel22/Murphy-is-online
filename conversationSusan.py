from email import message
import pygame
pygame.init()

from textes import *

police = pygame.font.SysFont('Lucida' ,20)

Susan0_1 = police.render("Ceci est le début de votre conversation avec Susan:",1,(100,100,100))
Susan0_2 = police.render("Les messages envoyés dans cette conversations, ",1,(100,100,100))
Susan0_3 = police.render("sont désormais protégés avec le chiffrement. ",1,(100,100,100))
Susan0_4 = police.render("Pour avoir plus d'information n'hésitez pas à ",1,(100,100,100))
Susan0_5 = police.render("consulter notre site.",1,(100,100,100))

'''----------------------------------------------------------------------------------------------------'''

Susan1 = police.render("Coucou mon coeur comment tu vas ?",1,(100,100,100))
messageSusan1 = [Susan1]

'''----------------------------------------------------------------------------------------------------'''

SMurphy2_1 = police.render("Salut mon pousin, je vais très bien et toi ?",1,(100,100,100))
SMurphy2_2 = police.render("ça va normal et toi ?",1,(100,100,100))
SMurphy2_3 = police.render("Je suis désolé mais je crois que vous faites erreur sur la personne",1,(100,100,100))
messageMurphy2_1 = [SMuprhy2_1]
messageMurphy2_2 = [Smurphy2_2]
messageMurphy2_3 = [Smurphy2_3]
messageMurphy2 = [messageMurphy2_1, messageMurphy2_2, messageMuprhy2_3]

'''----------------------------------------------------------------------------------------------------'''
Susan3_1 = police.render("Je vais bien aussi, le trajet été un peu long mais je suis heureuse",1,(100,100,100))
Susan3_1_1 = police.render("d'avoir enfin retrouvé ma famille. Ils m'avait trop manqué !!",1,(100,100,100))
Susan3_2 = police.render("Moi ça va bien aussi mais toi tu n'as pas l'air d'aller bien :(",1,(100,100,100))
Susan3_3 = police.render("Mon poussin est ce que tu as bien pris tes médicament ?",1,(100,100,100))
messageSusan3_1 = [Susan3_1, Susan3_1_1 ]
messageSusan3_2 = [Susan3_2]
messageSusan3_3 = [Susan3_3]
messageSusan3 = [messageSusan3_1,messageSusan3_2,messageSusan3_3]

'''----------------------------------------------------------------------------------------------------'''

SMurphy4_1 = police.render("J'espère qu'ils vont tous bien !!",1,(100,100,100))
SMurphy4_2 = police.render("Comment t'as réussi à faire passer le temps durant le trajet ?",1,(100,100,100))
SMurphy4_3 = police.render("Tu m'en parlais tellement de ta famille, je suis content que tu les revois :)",1,(100,100,100))
messageMurphy4_1 = [SMuprhy4_1]
messageMurphy4_2 = [Smurphy4_2]
messageMurphy4_3 = [Smurphy4_3]
messageMurphy4 = [messageMurphy4_1, messageMurphy4_2, messageMuprhy4_3]

'''----------------------------------------------------------------------------------------------------'''

SMurphy5_1 = police.render("Si si ça va bien ne t'en fais pas !! tu fais quoi de beau ?",1,(100,100,100))
SMurphy5_2 = police.render("Je me sens très bizzare, je sais plus où je suis.",1,(100,100,100))
SMurphy5_3 = police.render("Je suis simplement fatigué. Bon tu fais quoi de beau ? ",1,(100,100,100))
messageMurphy5_1 = [SMuprhy5_1]
messageMurphy5_2 = [Smurphy5_2]
messageMurphy5_3 = [Smurphy5_3]
messageMurphy5 = [messageMurphy5_1, messageMurphy5_2, messageMuprhy5_3]

'''----------------------------------------------------------------------------------------------------'''

SMurphy6_1 = police.render("De quels médicaments ?",1,(100,100,100))
SMurphy6_2 = police.render("Je n'avais pas envie de les prendre.",1,(100,100,100))
SMurphy6_3 = police.render("Je me souviens avoir pris des médicaments ce matin. ",1,(100,100,100))
messageMurphy6_1 = [SMuprhy6_1]
messageMurphy6_2 = [Smurphy6_2]
messageMurphy6_3 = [Smurphy6_3]
messageMurphy6 = [messageMurphy6_1, messageMurphy6_2, messageMuprhy6_3]

'''----------------------------------------------------------------------------------------------------'''
Susan7_1 = police.render("Oui ils vont tous bien, ils te passent tous le bonjours !!",1,(100,100,100))
Susan7_1_1 = police.render("Ils auraient voulu que tu sois là.",1,(100,100,100))
Susan7_2 = police.render("J'ai passé le trajet un organiser notre week-end pour aller voir Artick Monkeys !!",1,(100,100,100))
Susan7_3 = police.render("Ils m'avaient trooop manqué, mais maintenant c'est toi qui me manque <3",1,(100,100,100))
messageSusan7_1 = [Susan7_1, Susan7_1_1 ]
messageSusan7_2 = [Susan7_2]
messageSusan7_3 = [Susan7_3]
messageSusan7 = [messageSusan7_1,messageSusan7_2,messageSusan7_3]

'''----------------------------------------------------------------------------------------------------'''
Susan8_1 = police.render("Je suis avec ma famille et toi mon coeur ? ",1,(100,100,100))
Susan8_2 = police.render("Je savais que je n'aurai pas du te laisser seul!",1,(100,100,100))
Susan8_2_1 = police.render("ça doit surement être l'effet des médicament, il faut que tu te reposes un peu",1,(100,100,100))
Susan8_3 = police.render("Je suis avec ma famille mon coeur, vas te reposer si t'es fatigué !!",1,(100,100,100))
messageSusan8_1 = [Susan8_1]
messageSusan8_2 = [Susan8_2, Susan8_2_1]
messageSusan8_3 = [Susan8_3]
messageSusan8 = [messageSusan8_1,messageSusan8_2,messageSusan8_3]

'''----------------------------------------------------------------------------------------------------'''
Susan8_1 = police.render("Merde !! Pourtant j'avais prévenue Taylor qu'il devait t'aider à les prendre.",1,(100,100,100))
Susan8_1_1 = police.render("Ne bouge surtout pas je vais lui envoyer un message.",1,(100,100,100))
Susan8_2 = police.render("Merde !! Pourtant j'avais prévenue Taylor qu'il devait t'aider à les prendre",1,(100,100,100))
Susan8_2_1 = police.render("Ne bouge surtout pas je vais lui envoyer un message",1,(100,100,100))
Susan8_3 = police.render("La psychiatre a dit que c'était normal que ça faisse cela. repose toi un peu !!",1,(100,100,100))
messageSusan8_1 = [Susan8_1, Susan8_1_1 ]
messageSusan8_2 = [Susan8_2, Susan8_2_1]
messageSusan8_3 = [Susan8_3]
messageSusan8 = [messageSusan8_1,messageSusan8_2,messageSusan8_3]

'''----------------------------------------------------------------------------------------------------'''

SMurphy9_1 = police.render("Ohh c'est gentil tu leur passeras le bonjour de ma part !!",1,(100,100,100))
SMurphy9_2 = police.render("J'aurai voulu aussi les rencontrer mais bon...'",1,(100,100,100))
SMurphy9_3 = police.render("Une prochaine fois, vous avez prévue de faire un truc ?",1,(100,100,100))
messageMurphy9_1 = [SMuprhy9_1]
messageMurphy9_2 = [Smurphy9_2]
messageMurphy9_3 = [Smurphy9_3]
messageMurphy9 = [messageMurphy9_1, messageMurphy9_2, messageMuprhy9_3]

'''----------------------------------------------------------------------------------------------------'''

SMurphy10_1 = police.render("Trop coool !! j'ai tellement d'aller les voir.",1,(100,100,100))
SMurphy10_2 = police.render("Mais je t'avais dit que t'étais pas obligé de te prendre la tête",1,(100,100,100))
SMurphy10_3 = police.render("et alors on y va quand ?",1,(100,100,100))
messageMurphy10_1 = [SMuprhy10_1]
messageMurphy10_2 = [Smurphy10_2]
messageMurphy10_3 = [Smurphy10_3]
messageMurphy10 = [messageMurphy10_1, messageMurphy10_2, messageMuprhy10_3]

'''----------------------------------------------------------------------------------------------------'''

SMurphy11_1 = police.render("Tu me manques trop aussi !!!",1,(100,100,100))
SMurphy11_2 = police.render("J'ai trop hate de te revoir <3",1,(100,100,100))
SMurphy11_3 = police.render("On se revoit vite.",1,(100,100,100))
messageMurphy11_1 = [SMuprhy11_1]
messageMurphy11_2 = [Smurphy11_2]
messageMurphy11_3 = [Smurphy11_3]
messageMurphy11 = [messageMurphy11_1, messageMurphy11_2, messageMuprhy11_3]

'''----------------------------------------------------------------------------------------------------'''

SMurphy12_1 = police.render("Je vais me reposer, je viens de prendre mes médicament.",1,(100,100,100))
SMurphy12_2 = police.render("Je fais pas grand chose, je sais plus où je suis exactement.",1,(100,100,100))
SMurphy12_3 = police.render("Je suis simplement entrain de te parler",1,(100,100,100))
messageMurphy12_1 = [SMuprhy12_1]
messageMurphy12_2 = [Smurphy12_2]
messageMurphy12_3 = [Smurphy12_3]
messageMurphy12 = [messageMurphy12_1, messageMurphy12_2, messageMuprhy12_3]

'''----------------------------------------------------------------------------------------------------'''

SMurphy13_1 = police.render("Est ce que je dois me méfier de la psychiatre ?",1,(100,100,100))
SMurphy13_2 = police.render("Pourquoi je continue à les prendre s'ils me font perdre la mémoire ?",1,(100,100,100))
SMurphy13_3 = police.render("Est ce que c'est une bonne psychiatre ?",1,(100,100,100))
messageMurphy13_1 = [SMuprhy13_1]
messageMurphy13_2 = [Smurphy13_2]
messageMurphy13_3 = [Smurphy13_3]
messageMurphy13 = [messageMurphy13_1, messageMurphy13_2, messageMuprhy13_3]

'''----------------------------------------------------------------------------------------------------'''

SMurphy14_1 = police.render("Est ce que je dois me méfier de Taylor ?",1,(100,100,100))
SMurphy14_2 = police.render("Est ce qu'il a fait exprès ?",1,(100,100,100))
SMurphy14_3 = police.render("Qui est Taylor ?",1,(100,100,100))
messageMurphy14_1 = [SMuprhy14_1]
messageMurphy14_2 = [Smurphy14_2]
messageMurphy14_3 = [Smurphy14_3]
messageMurphy14 = [messageMurphy14_1, messageMurphy14_2, messageMuprhy14_3]

'''----------------------------------------------------------------------------------------------------'''

messageMurphy15 = [messageMurphy13_1, messageMurphy13_2, messageMuprhy13_3]

'''----------------------------------------------------------------------------------------------------'''
Susan16_1 = police.render("Bon je dois te laisser, je vais devoir aller passer un peu de temps avec ma",1,(100,100,100))
Susan16_1_1 = police.render("famille. J'ai hate qu'on se revoit et qu'on aille voir ton groupe préféré ",1,(100,100,100))
Susan16_1_2 = police.render("le week-end de mon retour. J'espère que tu vas adorer !!!",1,(100,100,100))
messageSusan16_1 = [Susan16_1, Susan16_1_1, Susan16_1_2 ]
messageSusan16 = [messageSusan16_1]

'''----------------------------------------------------------------------------------------------------'''
Susan17_1 = police.render("Meme reponse que pour noah",1,(100,100,100))
Susan17_2 = police.render("La psychiatre a dit qu'il ne fallait surout pas t'arrêter sinon t'allais",1,(100,100,100))
Susan17_2_1 = police.render("refaire une rechute.",1,(100,100,100))
Susan17_3 = police.render("Meme réponse que pour Susan17_1",1,(100,100,100))
messageSusan17_1 = [Susan17_1]
messageSusan17_2 = [Susan17_2, Susan17_2_1]
messageSusan17_3 = [Susan17_3]
messageSusan17 = [messageSusan17_1, messageSusan17_2, messageSusan17_3]

'''----------------------------------------------------------------------------------------------------'''
Susan18_1 = police.render("Meme reponse que pour noah",1,(100,100,100))
Susan18_2 = police.render("C'est vrai qu'il ne te porte pas dans son coeur, mais de la à faire une chose",1,(100,100,100))
Susan18_2_1 = police.render("pareille je ne pense pas.",1,(100,100,100))
Susan18_3 = police.render("Alors là tu ne vas vraiment pas bien, je lui envoie un message tout de suite.",1,(100,100,100))
messageSusan18_1 = [Susan18_1]
messageSusan18_2 = [Susan18_2, Susan18_2_1]
messageSusan18_3 = [Susan18_3]
messageSusan18 = [messageSusan18_1, messageSusan18_2, messageSusan18_3]