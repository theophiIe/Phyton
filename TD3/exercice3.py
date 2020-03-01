print "Ecrire une chaine de caratere :",
sequence = raw_input()
i = 0
cmptC = 0
cmptM = 0
#Compter le nombre de C et de M#

while i<len(sequence):
	if sequence[i] in "C": 
		cmptC = cmptC + 1
		
	if sequence[i] in "M" :
		cmptM = cmptM + 1
	i = i + 1

print "Nombre de cysteine :", cmptC
print "Nombre de metianine :", cmptM
