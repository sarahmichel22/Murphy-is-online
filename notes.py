import pygame
pygame.init()

from textes import *
from classes import *

police = pygame.font.SysFont('Lucida' ,20)

Date1 = police.render("11/12",1,(251,251,64))

Note1_1 = police.render("Cela fait quelques semaines maintenant que mon fils à disparu, je continue de mon",1,(100,100,100))
Note1_2 = police.render("côté à enquêter sur des pistes qui pourraient me conduire à mon enfant. La police  ",1,(100,100,100))
Note1_3 = police.render("n'a toujours pas d'éléments concrets qui pourraient faire avancer l'enquête, ils ",1,(100,100,100))
Note1_4 = police.render("supposent qu'une personne de mon entourage pourrait être le coupable, je n'y",1,(100,100,100))
Note1_5 = police.render("crois pas une seconde.",1,(100,100,100))

Date2 = police.render("25/12",1,(251,251,64))

Note2_1 = police.render("Aujourd'hui était un jour très compliqué. Bien sûr, Victoria et moi n'avons pas le",1,(100,100,100))
Note2_2 = police.render("moral de célébrer les fêtes de fin d'année et nous avons refusé toutes les invitations ",1,(100,100,100))
Note2_3 = police.render("de nos amis. Mon fils me manque...",1,(100,100,100))
Note2_4 = police.render("J'aimerai qu'il soit parmi nous mais je ne désespère pas, nous parviendrons à le",1,(100,100,100))
Note2_5 = police.render("retrouver. Comme par miracle, j'ai reçu la carte d'une psychiatre dans ma boîte ",1,(100,100,100))
Note2_6 = police.render("aux lettres ce matin, j'ai vraiment besoin d'aller consulter. Je prendrais rendez-vous",1,(100,100,100))
Note2_6 = police.render("chez elle bientôt.",1,(100,100,100))

Date3 = police.render("03/02",1,(251,251,64))

Note3_1 = police.render("Plus le temps passe et moins je ne souhaite passer de temps avec Victoria, elle ",1,(100,100,100))
Note3_2 = police.render("m'agace, je vais passer un peu de temps seul désormais et aller voir des gens ",1,(100,100,100))
Note3_3 = police.render("pour me changer les idées.",1,(100,100,100))

Date4 = police.render("05/02",1,(251,251,64))

Note4_1 = police.render("Hier je suis allé rendre visite à mon frère Taylor, il n'arrête pas de me parler de",1,(100,100,100))
Note4_2 = police.render("Susan, une ancienne amie, il a l'air fou amoureux d'elle mais cela n'a pas l'air",1,(100,100,100))
Note4_3 = police.render("réciproque.",1,(100,100,100))
Note4_4 = police.render("Susan a toujours eu une attirance pour moi et Taylor m'en a toujours voulu pour ",1,(100,100,100))
Note4_5 = police.render("ça et notre relation a énormément changé depuis qu'il éprouve autant de jalousie. ",1,(100,100,100))
Note4_6 = police.render("J'ai été très étonné qu'il m'invite chez lui pour cette même raison.",1,(100,100,100))

Date5 = police.render("12/02",1,(251,251,64))

Note5_1 = police.render("Taylor m'a de nouveau invité chez lui sans me prévenir qu'il y aurait Susan. Je ne",1,(100,100,100))
Note5_2 = police.render("comprends pas son attitude, j'ai l'impression qu'il cherhce à me tester et à savoir",1,(100,100,100))
Note5_3 = police.render("si je pourrais le trahir pour elle. J'ai l'impression qu'il prépare un mauvais coup.",1,(100,100,100))

Date6 = police.render("15/03",1,(251,251,64))

Note6_1 = police.render("Premier rendez-vous chez la psychiatre Dr.Davies, elle a accepté de me prendre ",1,(100,100,100))
Note6_2 = police.render("en charge très rapidement, nous avons beaucoup discuté et elle semble très ",1,(100,100,100))
Note6_3 = police.render("proffessionnelle. A la fin de notre séance je me sentais légèrement plus apaisé.",1,(100,100,100))

Date7 = police.render("20/03",1,(251,251,64))

Note7_1 = police.render("Susan m'a invité à prendre un café aujourd'hui, j'y suis allé en cachette de Victoria",1,(100,100,100))
Note7_2 = police.render("pour ne pas qu'elle s'énerve. Je suis resté assez distant au cas où tout cela ne serait",1,(100,100,100))
Note7_3 = police.render("qu'un stratagème de mon frère.",1,(100,100,100))

Date8 = police.render("25/03",1,(251,251,64))

Note8_1 = police.render("Hier soir je suis rentré complètement saoul chez nous, malgré les appels insistants ",1,(100,100,100))
Note8_2 = police.render("de Victoria qui m'implorait de rentrer à la maison. Je ne veux pas lui faire de la ",1,(100,100,100))
Note8_3 = police.render("peine mais je n'en peux plus d'elle. J'aimerai qu'elle disparaisse parfois.",1,(100,100,100))

Date9 = police.render("01/04",1,(251,251,64))

Note9_1 = police.render("Hier après-midi, alors que je devais partir au travail, Susan m'a invité à passer boire",1,(100,100,100))
Note9_2 = police.render("un verre chez elle. J'étais très agacé par l'attitude de Victoria ces derniers temps que ",1,(100,100,100))
Note9_3 = police.render("j'ai fini par accepter. Nous avons finis par passer la nuit ensemble et je ne suis rentré",1,(100,100,100))
Note9_4 = police.render("chez moi qu'au matin. ",1,(100,100,100))
Note9_5 = police.render("Victoria était folle de rage. Néanmoins, je ne ressentais aucun remord concernant ce ",1,(100,100,100))
Note9_6 = police.render("qui s'était passé et je lui ai délibérément menti.",1,(100,100,100))

Date10 = police.render("05/04",1,(251,251,64))

Note10_1 = police.render("Le Dr.Davies m'a prescrit des antidépresseurs tout récemment et je ressens les ",1,(100,100,100))
Note10_2 = police.render("bienfait de ces derniers, je me sens revivre petit à petit.",1,(100,100,100))

Date11 = police.render("20/04",1,(251,251,64))

Note11_1 = police.render("Victoria m'a annocé qu'elle avait pris rendez-vous chez le notaire pour divorcer, ce",1,(100,100,100))
Note11_2 = police.render("fût un énorme choc pour moi. Elle ne veut plus habiter avec moi jusqu'au jour du",1,(100,100,100))
Note11_3 = police.render("divorce et m'a jeté de chez moi. Je suis parti me consoler chez Susan qui avait",1,(100,100,100))
Note11_4 = police.render("l'air très heureuse de la situation. Elle a toujours détesté Victoria car elle aurait aimé ",1,(100,100,100))
Note11_5 = police.render("être à sa place et a tenté à nombreuses reprises de nous faire séparer, elle semblait",1,(100,100,100))
Note11_6 = police.render("avoir enfin réussi son coup. Je me demande comment j'ai pu l'ignorer pendant aussi ",1,(100,100,100))
Note11_7 = police.render("longtemps, même si nous avions déjà échnagé de petits bisous quand nous étions ",1,(100,100,100))
Note11_8 = police.render("jeune, je n'ai jamais considéré que notre histoire pouvait devenir sérieuse. Elle est ",1,(100,100,100))
Note11_9 = police.render("tout ce que je recherche et me fait me sentir de nouveau vivant.",1,(100,100,100))
Note11_10 = police.render("J'aime la retrouver le soir et imaginer que j'ai de nouveau 20 ans.",1,(100,100,100))

Date12 = police.render("30/06",1,(251,251,64))

Note12_1 = police.render("J'ai aménagé avec Susan après que le divorce soit prononcé. Nous avions une vie",1,(100,100,100))
Note12_2 = police.render("tranquille. Après le divorce, ma psychiatre m'a prescrit de nouveaux médicaments,",1,(100,100,100))
Note12_3 = police.render("plus fort, ceux-ci me permet de tenir le coup.",1,(100,100,100))
Note12_4 = police.render("Le plus dur a bien sûr été d'annoncer à mon frère que je sortais avec Susan. Il m'a ",1,(100,100,100))
Note12_5 = police.render("insulté de tous les noms. Il ne m'aimait déjà pas beaucoup mais cette fois je pouvais",1,(100,100,100))
Note12_6 = police.render("ressentir une haine si grande en lui, qu'il aurai pu me tuer si Susan n'était pas ",1,(100,100,100))
Note12_7 = police.render("avec nous. Je dois dire que je l'ai bien cherché, mais il ne m'a jamais montré son",1,(100,100,100))
Note12_8 = police.render("affection et au contraire sans arrêt me nuire.",1,(100,100,100))

Date13 = police.render("01/07",1,(251,251,64))

Note13_1 = police.render("J'ai de plus en plus de mal à me rappeler de petits événements comme ce que j'ai",1,(100,100,100))
Note13_2 = police.render("mangé dans la journée ou encore si j'ai bien fermé la porte. Cela devient très ",1,(100,100,100))
Note13_3 = police.render("handicapant à la longue La psychiatre m'a formellement assuré que cela n'empirerait",1,(100,100,100))
Note13_4 = police.render("pas avec le temps et qu'il était primordial pour moi de continuer mon traitement ",1,(100,100,100))
Note13_5= police.render("pour ne pas subir une nouvelle rechute. ",1,(100,100,100))


notesliste = [Date1,Note1_1,Note1_2,Note1_3,Note1_4,Note1_5,Date2,Note2_1,Note2_2,Note2_3,Note2_4,Note2_5,Note2_6,Date3,Note3_1,Note3_2,Note3_3,Date4,Note4_1,Note4_2,Note4_3,Note4_4,Note4_5,Note4_6,Date5,Note5_1,Note5_2,Note5_3,Date6,Note6_1,Note6_2,Note6_3,Date7,Note7_1,Note7_2,Note7_3,Date8,Note8_1,Note8_2,Note8_3,Date9,Note9_1,Note9_2,Note9_3,Note9_4,Note9_5,Note9_6,Date10,Note10_1,Note10_2,Date11,Note11_1,Note11_2,Note11_3,Note11_4,Note11_5,Note11_6,Note11_7,Note11_8,Note11_9,Note11_10,Date12,Note12_1,Note12_2,Note12_3,Note12_4,Note11_5,Note12_6,Note12_7,Note12_8,Date13,Note13_1,Note13_2,Note13_3,Note13_4,Note13_5]

#def affichernotes(screen,premierenote):

def afficherChiffres(chiffre1,chiffre2,chiffre3,chiffre4,screen):
	if chiffre1 == 0:
		screen.blit(zero2,(453,180))
	elif chiffre1 == 1:
		screen.blit(un2,(453,180))
	elif chiffre1 == 2:
		screen.blit(deux2,(453,180))
	elif chiffre1 == 3:
		screen.blit(trois2,(453,180))
	elif chiffre1 == 4:
		screen.blit(quatre2,(453,180))
	elif chiffre1 == 5:
		screen.blit(cinq2,(453,180))
	elif chiffre1 == 6:
		screen.blit(six2,(453,180))
	elif chiffre1 == 7:
		screen.blit(sept2,(453,180))
	elif chiffre1 == 8:
		screen.blit(huit2,(453,180))
	elif chiffre1 == 9:
		screen.blit(neuf2,(453,180))

	if chiffre2 == 0:
		screen.blit(zero2,(533,180))
	elif chiffre2 == 1:
		screen.blit(un2,(533,180))
	elif chiffre2 == 2:
		screen.blit(deux2,(533,180))
	elif chiffre2 == 3:
		screen.blit(trois2,(533,180))
	elif chiffre2 == 4:
		screen.blit(quatre2,(533,180))
	elif chiffre2 == 5:
		screen.blit(cinq2,(533,180))
	elif chiffre2 == 6:
		screen.blit(six2,(533,180))
	elif chiffre2 == 7:
		screen.blit(sept2,(533,180))
	elif chiffre2 == 8:
		screen.blit(huit2,(533,180))
	elif chiffre2 == 9:
		screen.blit(neuf2,(533,180))

	if chiffre3 == 0:
		screen.blit(zero2,(613,180))
	elif chiffre3 == 1:
		screen.blit(un2,(613,180))
	elif chiffre3 == 2:
		screen.blit(deux2,(613,180))
	elif chiffre3 == 3:
		screen.blit(trois2,(613,180))
	elif chiffre3 == 4:
		screen.blit(quatre2,(613,180))
	elif chiffre3 == 5:
		screen.blit(cinq2,(613,180))
	elif chiffre3 == 6:
		screen.blit(six2,(613,180))
	elif chiffre3 == 7:
		screen.blit(sept2,(613,180))
	elif chiffre3 == 8:
		screen.blit(huit2,(613,180))
	elif chiffre3 == 9:
		screen.blit(neuf2,(613,180))

	if chiffre4 == 0:
		screen.blit(zero2,(693,180))
	elif chiffre4 == 1:
		screen.blit(un2,(693,180))
	elif chiffre4 == 2:
		screen.blit(deux2,(693,180))
	elif chiffre4 == 3:
		screen.blit(trois2,(693,180))
	elif chiffre4 == 4:
		screen.blit(quatre2,(693,180))
	elif chiffre4 == 5:
		screen.blit(cinq2,(693,180))
	elif chiffre4 == 6:
		screen.blit(six2,(693,180))
	elif chiffre4 == 7:
		screen.blit(sept2,(693,180))
	elif chiffre4 == 8:
		screen.blit(huit2,(693,180))
	elif chiffre4 == 9:
		screen.blit(neuf2,(693,180))


def supprimernombre(chiffre1,chiffre2,chiffre3,chiffre4):
		if chiffre4<10:
			chiffre4=10
			return chiffre4
		elif chiffre3<10:
			chiffre3=10
			return chiffre3
		elif chiffre2<10:
			chiffre2=10	
			return chiffre2
		elif chiffre1<10:
			chiffre1=10
			return chiffre1


def validermdp(chiffre1,chiffre2,chiffre3,chiffre4):
	if chiffre1==2 and chiffre2==0 and chiffre3==0 and chiffre4==2:
		return True
	else :
		return False