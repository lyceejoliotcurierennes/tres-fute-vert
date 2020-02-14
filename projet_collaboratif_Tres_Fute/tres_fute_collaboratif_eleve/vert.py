##################
### Très futé ####
##################
## partie verte ##
##################
## Co-auteurs : Idir, Lauryne, Robin
#################


## initialisation de la grille verte
def init_vert():
	#
	# à compléter
	liste=[False for i in range(1)]
    #return à modifier
	return None


## affichage de la grille verte :
def affiche_vert(grille):
	#
	print(grille)
	#
	print()
    
## test de positionnement du dé dans la grille verte    
def test_vert(couleur,des,grille,bonus):
    # peut on positionner le dé
	impossible = True
	# tuple des contraintes
	tuple_vert = (1,2,3,4,5,1,2,3,4,5,6)
	# recherche de la premiere case vide
	i = 0
	while i < len(grille) - 1 and grille[i+1]>0:
		i = i+1
	if i == 10 and grille[1]>0 : # la grille est pleine
		print('la grille est pleine')
	else : # positionnement du dé
		if tuple_vert[i+1]<=des[couleur]:
			grille[i+1]=des[couleur]
			impossible = false
		else :
			print('Vous ne pouvez pas placer le dé dans cette grille')
		
	#return à modifier
	return impossible,des,grille,bonus

# décompte des points de la grille
def decompte_vert(grille) :
	total = 0
    #
	# à compléter
	#
	return total
