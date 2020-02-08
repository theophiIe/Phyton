print "Ecrire une chaine de caratere"
chaine = raw_input()

print "Afficher le debut ou la fin d'une chaine taper D ou F"
reponse = raw_input() 
reponse = reponse.upper()

if reponse == "D" : 
	print "nombre de caractere a afficher de la chaine en partant du debut :"
	nbreCara = int(input())
	print chaine[:nbreCara]

elif reponse == "F" :
	print "\nNombre de caractere a afficher de la chaine en partant du la fin :"
	nbreCara = int(input())
	print chaine[len(chaine)-nbreCara:]

else :
	 print "erreur dans la reponse"
