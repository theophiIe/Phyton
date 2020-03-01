print "premiere chaine de caractere :",
chaine1 = raw_input()
print "seconde chaine de caractere :",
chaine2 = raw_input()

if chaine1.count(chaine2) > 0 : 
	print "La chaine 2 est presente dans la chaine 1"
else :
	print "La chaine 2 n'est pas presente dans la chaine 1"

if chaine2 in chaine1 :
	print "La chaine 2 est presente dans la chaine 1"
else :
	print "La chaine 2 n'est pas presente dans la chaine 1"
