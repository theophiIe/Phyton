fichier = open("sequence.txt", "r")	

inutile = fichier.readline()
seq = fichier.readline()

mini = input("taille mini : ")
stop = "TGA/TAA/TGA"

g=""
i=0
start = -1

while i<len(seq)-2:
	if start < 0 and seq[i:i+3] == "ATG" :
		start = 1
	
	elif start >= 0 and seq[i:i+3] in stop : 
		if i + 3 - start >= mini : 
			g.write("+1\t" + str(start) + "\t" + str(i+2) + "\t")
			
		start = -1
	i=i+3
	
