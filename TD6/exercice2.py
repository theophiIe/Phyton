while(1):
	nameFile = raw_input("Le nom du fichier : ")
	try : 
		f = open(nameFile, "r")	
		break
	except :
		print "erreur nom fichier"

seq = ""
ligne = f.readline() 

while(ligne != "") :
	seq = seq + ligne[:len(ligne)-1]
	ligne = f.readline()

f.close()

seqNucl = raw_input("Sequence nucleique a rechercher : ")
seqNucl = seqNucl.upper()

n = 0
occurence = 0
val = ""

while n!=len(seq) : 
	if seqNucl in seq :
		occrence = n + 1
	n = n+1

print occurence


