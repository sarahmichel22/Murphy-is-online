import pygame
pygame.init()

from textes import *

police = pygame.font.SysFont('Lucida' ,20)

Date1 = police.render("11/12",1,(100,100,100))

Note1_1 = police.render("Cela fait quelques semaines maintenant que mon fils à disparu,",1,(100,100,100))
Note1_2 = police.render("je continue de mon côté à enquêter sur des pistes qui pourraient ",1,(100,100,100))
Note1_3 = police.render("me conduire à mon enfant.",1,(100,100,100))
Note1_4 = police.render("La police n'a toujours pas d'éléments concrets qui pourraient faire",1,(100,100,100))
Note1_5 = police.render("avancer l'enquête, ils supposent qu'une personne de mon entourage ",1,(100,100,100))
Note1_6 = police.render("pourrait êtrele coupable, je n'y crois pas une seconde.",1,(100,100,100))

Date2 = police.render("25/12",1,(100,100,100))

Note2_1 = police.render("Aujourd'hui était un jour très compliqué. Bien sûr, Victoria et moi",1,(100,100,100))
Note2_2 = police.render("n'avons pas le moral de célébrer les fêtes de fin d'année et nous avons",1,(100,100,100))
Note2_3 = police.render("refusé toutes les invitations de nos amis. Mon fils me manque...",1,(100,100,100))
Note2_4 = police.render("J'aimerai qu'il soit parmi nous mais je ne désespère pas, nous parviendrons",1,(100,100,100))
Note2_5 = police.render("à le retrouver.",1,(100,100,100))
Note2_6 = police.render("Comme par miracle, j'ai reçu la carte d'une psychiatre dans ma boîte aux ",1,(100,100,100))
Note2_7 = police.render("lettres ce matin, j'ai vraiment besoin d'aller consulter.",1,(100,100,100))
Note2_8 = police.render("Je prendrais rendez-vous chez elle bientôt.",1,(100,100,100))

Date3 = police.render("03/02",1,(100,100,100))

Note3_1 = police.render("Plus le temps passe et moins je ne souhaite passer de temps avec Victoria,",1,(100,100,100))
Note3_2 = police.render("elle m'agace, je vais passer un peu de temps seul désormais et aller voir ",1,(100,100,100))
Note3_3 = police.render("des gens pour me changer les idées.",1,(100,100,100))

Date4 = police.render("05/02",1,(100,100,100))

Note4_1 = police.render("Hier je suis allé rendre visite à mon frère Taylor, il n'arrête pas de me",1,(100,100,100))
Note4_2 = police.render("parler de Susan, une ancienne amie, il a l'air fou amoureux d'elle mais cela ",1,(100,100,100))
Note4_3 = police.render("n'a pas l'air réciproque.",1,(100,100,100))
Note4_4 = police.render("Susan a toujours eu une attirance pour moi et Taylor m'en a toujours voulu pour ",1,(100,100,100))
Note4_5 = police.render("ça et notre relation a énormément changé depuis qu'il éprouve autant de jalousie. ",1,(100,100,100))
Note4_6 = police.render("J'ai été très étonné qu'il m'invite chez lui pour cette même raison.",1,(100,100,100))

Date5 = police.render("12/02",1,(100,100,100))

Note5_1 = police.render("Taylor m'a de nouveau invité chez lui sans me prévenir qu'il y aurait Susan.",1,(100,100,100))
Note5_2 = police.render("Je ne comprends pas son attitude, j'ai l'impression qu'il cherhce à me tester",1,(100,100,100))
Note5_3 = police.render("et à savoir si je pourrais le trahir pour elle. J'ai l'impression qu'il prépare",1,(100,100,100))
Note5_4 = police.render("un mauvais coup.",1,(100,100,100))

Date6 = police.render("15/03",1,(100,100,100))

Note6_1 = police.render("Premier rendez-vous chez la psychiatre Dr.Davies, elle a accepté de me prendre",1,(100,100,100))
Note6_2 = police.render("en charge très rapidement, nous avons beaucoup discuté et elle semble très",1,(100,100,100))
Note6_3 = police.render("proffessionnelle. A la fin de notre séance je me sentais légèrement plus apaisé.",1,(100,100,100))

Date7 = police.render("20/03",1,(100,100,100))

Note7_1 = police.render("Susan m'a invité à prendre un café aujourd'hui, j'y suis allé en cachette de Victoria",1,(100,100,100))
Note7_2 = police.render("pour ne pas qu'elle s'énerve. Je suis resté assez distant au cas où tout cela ne serait",1,(100,100,100))
Note7_3 = police.render("qu'un stratagème de mon frère.",1,(100,100,100))

Date8 = police.render("25/03",1,(100,100,100))

Note8_1 = police.render("Hier soir je suis rentré complètement saoul chez nous, malgré les appels insistants de ",1,(100,100,100))
Note8_2 = police.render("Victoria qui m'implorait de rentrer à la maison. Je ne veux pas lui faire de la peine ",1,(100,100,100))
Note8_3 = police.render("mais je n'en peux plus d'elle.",1,(100,100,100))
Note8_4 = police.render("J'aimerai qu'elle disparaisse parfois.",1,(100,100,100))

Date9 = police.render("01/04",1,(100,100,100))

Note9_1 = police.render("Hier après-midi, alors que je devais partir au travail, Susan m'a invité à passer boire",1,(100,100,100))
Note9_2 = police.render("un verre chez elle. J'étais très agacé par l'attitude de Victoria ces derniers temps que ",1,(100,100,100))
Note9_3 = police.render("j'ai fini par accepter. Nous avons finis par passer la nuit ensemble et je ne suis rentré",1,(100,100,100))
Note9_4 = police.render("chez moi qu'au matin. ",1,(100,100,100))
Note9_5 = police.render("Victoria était folle de rage. Néanmoins, je ne ressentais aucun remord concernant ce qui",1,(100,100,100))
Note9_6 = police.render("s'était passé et je lui ai délibérément menti.",1,(100,100,100))

Date10 = police.render("05/04",1,(100,100,100))

Note10_1 = police.render("Le Dr.Davies m'a prescrit des antidépresseurs tout récemment et je ressens les bienfait",1,(100,100,100))
Note10_2 = police.render("de ces derniers, je me sens revivre petit à petit.",1,(100,100,100))

Date11 = police.render("20/04",1,(100,100,100))

Note11_1 = police.render("Victoria m'a annocé qu'elle avait pris rendez-vous chez le notaire pour divorcer,",1,(100,100,100))
Note11_2 = police.render("ce fût un énorme choc pour moi. Elle ne veut plus habiter avec moi jusqu'au jour",1,(100,100,100))
Note11_3 = police.render("du divorce et m'a jeté de chez moi. Je suis parti me consoler chez Susan qui avait",1,(100,100,100))
Note11_4 = police.render("néanmoins l'air très heureuse de la situation. Elle a toujours détesté Victoria caar",1,(100,100,100))
Note11_5 = police.render("elle aurait aimé être à sa place et a tenté à nombreuses reprises de nous faire séparer,",1,(100,100,100))
Note11_6 = police.render("elle semblait avoir enfin réussi son coup. Je me demande comment j'ai pu l'ignorer pendant",1,(100,100,100))
Note11_7 = police.render("aussi longtemps, même si nous avions déjà échnagé de petits bisous quand nous étions jeune,",1,(100,100,100))
Note11_8 = police.render("je n'ai jamais considéré que notre histoire pouvait devenir sérieuse. Elle est tout ce que",1,(100,100,100))
Note11_9 = police.render("je recherche et me fait me sentir de nouveau vivant.",1,(100,100,100))
Note11_10 = police.render("J'aime la retrouver le soir et imaginer que j'ai de nouveau 20 ans.",1,(100,100,100))

Date12 = police.render("30/06",1,(100,100,100))

Note12_1 = police.render("J'ai aménagé avec Susan après que le divorce soit prononcé. Nous avions une vie tranquille.",1,(100,100,100))
Note12_2 = police.render("Après le divorce, ma psychiatre m'a prescrit de nouveaux médicaments, plus fort, ceux-ci me",1,(100,100,100))
Note12_3 = police.render("permet de tenir le coup.",1,(100,100,100))
Note12_4 = police.render("Le plus dur a bien sûr été d'annoncer à mon frère que je sortais avec Susan. Il m'a insulté ",1,(100,100,100))
Note12_5 = police.render("de tous les noms. Il ne m'aimait déjà pas beaucoup mais cette fois je pouvais ressentir une",1,(100,100,100))
Note12_6 = police.render("haine si grande en lui, qu'il aurai pu me tuer si Susan n'était pas avec nous. ",1,(100,100,100))
Note12_7 = police.render("Je dois dire que je l'ai bien cherché, mais il ne m'a jamais montré son affection et au ",1,(100,100,100))
Note12_8 = police.render("contraire sans arrêt me nuire.",1,(100,100,100))

Date13 = police.render("01/07",1,(100,100,100))

Note13_1 = police.render("J'ai de plus en plus de mal à me rappeler de petits événements comme ce que j'ai mangé dans",1,(100,100,100))
Note13_2 = police.render("la journée ou encore si j'ai bien fermé la porte. Cela devient très handicapant à la longue",1,(100,100,100))
Note13_3 = police.render("La psychiatre m'a formellement assuré que cela n'empirerait pas avec le temps et qu'il était",1,(100,100,100))
Note13_4 = police.render("primordial pour moi de continuer mon traitement pour ne pas subir une nouvelle rechute. ",1,(100,100,100))
