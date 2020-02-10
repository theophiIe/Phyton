f = open("seq.txt", "r")
seq = ""
ligne = f.readline() 

while(ligne != "") :
		seq = seq + ligne[:len(ligne)-1]
		ligne = f.readline()
		
print seq
f.close()


#Autre facon
#ligne = ""

#with open("seq.txt", "r") as f:
#   for line in f.readlines():
#      ligne = ligne + line
		
#ligne = ligne.replace("\n", "")
#print ligne
	   
	   
