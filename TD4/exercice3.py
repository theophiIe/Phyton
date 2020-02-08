sequence = raw_input("la sequance : ")
erreur = 0
compteur = 0
i = 0
test = ""

while i < len(sequence) and test != "ERREUR" : 
	if sequence[i] not in "ACGT" : 
		erreur = i
		test = "ERREUR"
		
	i = i + 1

if test == "ERREUR" : 
	print "la sequence est fausse il y a une erreur en position : ", erreur
