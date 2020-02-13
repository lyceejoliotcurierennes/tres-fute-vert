##################
### Très futé ####
##################
## partie décompte
######

from jaune import *
from bleu import *
from vert import *
from orange import *
from violet import *

## les fonctions de décompte de chaque grille sont à compléter dans les fichiers couleur

#### Fonction de décompte des points au final ####


def decompte_points(grilles):
    decompte_grille={"jaune":decompte_jaune,"bleu":decompte_bleu,
                 "vert":decompte_vert,"orange":decompte_orange,
                 "violet":decompte_violet}
    total = 0
    for couleur in decompte_grille :
        sc_col = decompte_grille[couleur](grilles[couleur])
        print("score ",couleur," = ",sc_col)
        total = total + sc_col
    print("score final = ",total)