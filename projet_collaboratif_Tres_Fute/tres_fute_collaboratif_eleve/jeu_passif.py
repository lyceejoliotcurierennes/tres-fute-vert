##################
### Très futé ####
##################
## jeu passif   ##
##################
## Co-auteurs :
#################

# importation des modules

from random import randint
from jaune import *
from bleu import *
from vert import *
from orange import *
from violet import *
from bonus import *

## Fonction d'affichage des grilles avant de jouer
def affiche_grilles(grilles) :
    affichage={"jaune":affiche_jaune,"bleu":affiche_bleu,
                 "vert":affiche_vert,"orange":affiche_orange,
                 "violet":affiche_violet}
    for couleur in affichage :
        print("grille ",couleur," : ")
        affichage[couleur](grilles[couleur])


### Fonction de lancer des 6 dés
def lancer_des(des):
    for couleur in ("blanc","jaune","bleu","vert","orange","violet") :
        des[couleur]=[randint(1,6),0]
    return des


########
## Fonctions supplémentaires éventuelles
######

# à compléter éventuellement


###### 
## Fonction du jeu_actif à compléter
######
def jeu_passif(des,grilles,bonus):
    # liste des fonctions de grilles
    test_grille={"jaune":test_jaune,"bleu":test_bleu,
                 "vert":test_vert,"orange":test_orange,
                 "violet":test_violet}
    # lancer des 6 dés
    des = lancer_des(des)
    #
	# à compléter
	#
    return des,grilles,bonus
