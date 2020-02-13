##################
### Très futé ####
##################
## partie commune

# importation des modules

from random import randint
from jaune import *
from bleu import *
from vert import *
from orange import *
from violet import *
from jeu_actif import *
from jeu_passif import *
from bonus import *
from decompte import *
#from graphique import *

##########
## Initialisation du jeu
##########################

## initialisation des bonus stockables
def init_bonus():
    bonus={}
    bonus["relancer"]=0
    bonus["+1"]=0
    bonus["renard"]=0
    # à compléter éventuellement plus tard
    return bonus

## initialisation des grilles
def init_grilles():
    grilles={}
    grilles["jaune"]=init_jaune()
    grilles["bleu"]=init_bleu()
    grilles["vert"]=init_vert() 
    grilles["orange"]=init_orange()
    grilles["violet"]=init_violet()
    return grilles

## initialisation des dés
def init_des():
    des={}
    for couleur in ("blanc","jaune","bleu","vert","orange","violet") :
        des[couleur]=[randint(1,6),0]
    return des

##########
## Fonctions communes
########################

## affichage centralisé des grilles
#################
        
def affiche_grilles(grilles) :
    affichage={"jaune":affiche_jaune,"bleu":affiche_bleu,
                 "vert":affiche_vert,"orange":affiche_orange,
                 "violet":affiche_violet}
    for couleur in affichage :
        print("grille ",couleur," : ")
        affichage[couleur](grilles[couleur])

## Partie jeu
###############

# initialisations
def init_jeu():
    des=init_des()
    grilles=init_grilles()
    bonus=init_bonus()
    return des,grilles,bonus

# tour de jeu
def tour_de_jeu(n,des,grilles,bonus):
    print()
    print("tour actif n° ",n+1)
    jeu_actif(des,grilles,bonus)
    print()
    print("tour passif n° ",n+1)
    jeu_passif(des,grilles,bonus)
    return des,grilles,bonus

# partie
def jeu():
    # initialisation
    des,grilles,bonus=init_jeu()
    # tours de jeu
    for n in range(6) :
        tour_de_jeu(n,des,grilles,bonus)
        # gestion des bonus +1 et relancer à rajouter plus tard
    print("Le jeu est terminé.")
    affiche_grilles(grilles)
    decompte_points(grilles)
    
jeu()