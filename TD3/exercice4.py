print "Ecrire une chaine de caratere"
sequence = raw_input()
i = 0
nbreA = 0.0
nbreC = 0.0
nbreG = 0.0
nbreT = 0.0

while i < len(sequence):
	if(sequence[i] == "A") : 
		nbreA = nbreA + 1
		
	elif(sequence[i] == "C") : 
		nbreC = nbreC + 1
		
	elif(sequence[i] == "G") : 
		nbreG = nbreG + 1
		
	elif(sequence[i] == "T") : 
		nbreT = nbreT + 1
	
	i = i + 1

print "Pourcentage de A:", round(nbreA/len(sequence)*100,2),"%"
print "Pourcentage de C:", round(nbreC/len(sequence)*100,2),"%"
print "Pourcentage de G:", round(nbreG/len(sequence)*100,2),"%"
print "Pourcentage de T:", round(nbreT/len(sequence)*100,2),"%"
