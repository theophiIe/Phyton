print "Ecrire une sequence nucleotidique :"
seq = raw_input()
seq = seq.upper()

nbrA = float(seq.count('A'))
nbrC = float(seq.count('C'))
nbrG = float(seq.count('G'))
nbrT = float(seq.count('T'))

print "Pourcentage de A:", round(nbrA/len(seq)*100,2),"%"
print "Pourcentage de C:", round(nbrC/len(seq)*100,2),"%"
print "Pourcentage de G:", round(nbrG/len(seq)*100,2),"%"
print "Pourcentage de T:", round(nbrT/len(seq)*100,2),"%"

erreur = round(100 - ((nbrA/len(seq)*100)+(nbrC/len(seq)*100)+(nbrG/len(seq)*100)+(nbrT/len(seq)*100)),2)
print "Pourcentage d'erreur dans la sequence :", erreur, "%"
