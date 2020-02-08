sequence = raw_input("la sequance : ")
erreur = ""
compteur = 0
i = 0

while i < len(sequence) : 
	if sequence[i] not in "ACGT" : 
		erreur = erreur + str(i) + "," 
		compteur = compteur + 1
		
	i = i + 1

print "Nombre d'erreur ", compteur
print "Position des erreurs : ", erreur
