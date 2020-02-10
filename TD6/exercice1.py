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
while occurence != -1 : 
	occurence = seq.find(seqNucl,n)
	n = occurence + 1
	if occurence != -1 :
		occurence = occurence+1
		val = val + str(occurence) + ", "
		
g = open("occurenceEx1.txt", "w")
g.write(val)
g.close()

