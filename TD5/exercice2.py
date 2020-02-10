f = open("seq.txt", "r")
seq = ""
ligne = f.readline() 

while(ligne != "") :
		seq = seq + ligne[:len(ligne)-1]
		ligne = f.readline()

f.close()

g = open("seqExo2.txt", "w")

i=0
nbreA=0.0

while i < len(seq):
	if(seq[i] == "A") : 
		nbreA = nbreA + 1
	i = i + 1

g.write(seq + "\nPourcentage de A:" + str(round(nbreA/len(seq)*100,2)) + "%\nLa longeur de la sequance est : " + str(len(seq)))
g.close()
