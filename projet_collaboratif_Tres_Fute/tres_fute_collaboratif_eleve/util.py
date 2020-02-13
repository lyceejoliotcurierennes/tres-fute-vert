##################
### Très futé ####
##################
## util         ##
##################
## Co-auteurs :
#################

# fonction interne ( le _ empèche l'importation par import)
def _saisir(msg, valeurs_possibles):
    reponse = "blabla"
    while not reponse in valeurs_possibles:
        reponse = input(msg+str(valeurs_possibles)+" : ")
    return reponse

#----------------------------------
def saisir_de():
    valeurs_possibles = ("blanc", "jaune", "bleu", "vert", "orange", "violet")
    return _saisir("Quel dé ? ", valeurs_possibles)

#----------------------------------
def saisir_grille():
    valeurs_possibles = ("jaune", "bleu", "vert", "orange", "violet")
    return _saisir("Quelle grille pour le dé blanc ? ", valeurs_possibles)

#----------------------------------
def saisir_ligne():
    valeurs_possibles = ("0", "1", "2", "3")
    return int(_saisir("Entrer le numéro de ligne choisi parmi ", valeurs_possibles))

#----------------------------------
# à compléter éventuellement