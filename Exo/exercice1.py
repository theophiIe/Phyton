# ouverture du fichier sequence.txt
fichier = open("sequence.txt", "r")	

# lecture de la sequence
inutile = fichier.readline()
seq = fichier.readline()

# creation d'une liste avec la position du START
start = list(set(seq[i:].index('ATG') + i for i in xrange(len(seq)) if 'ATG' in seq[i:]))
start = sorted(start)

# creation de trois listes avec les positions des condons STOP
stop = list(set(seq[i:].index('TAA') + i for i in xrange(len(seq)) if 'TAA' in seq[i:]))
stopTGA = list(set(seq[i:].index('TGA') + i for i in xrange(len(seq)) if 'TGA' in seq[i:]))
stopTAG = list(set(seq[i:].index('TAG') + i for i in xrange(len(seq)) if 'TAG' in seq[i:]))

# concatenation des listes de codons STOP
stop.extend(stopTGA)
stop.extend(stopTAG)
stop = sorted(stop)

cmpt = 0
for cmpt in stop:
	print seq[stop[cmpt]:stop[cmpt]+3]
	#cmpt = cmpt + 1

# recherche du premier codon stop, recherche du start puis recherche condon stop

# PAS DE DECALAGE 
x = 0
y = 0

while ( x < len(stop) and y < len(start) ) :

	valStop = stop[x] % 3
	valStart = start[y] % 3

	if  (valStart == 0 and valStop == 0) and (start[y] > stop[x]) :
		
		x = x + 1
		valStop = stop[x] % 3
		
		while  valStop != 0 :
			valStop = stop[x] % 3
			if valStop == 0 and start[y] < stop[x]:
				print "position start : " + str(start[y] + 1) + "\t position du codon stop : " + str(stop[x] + 3)
				break
				
			elif valStop == 0 and start[y] > stop[x]:
				break
				
			x = x + 1
	
	elif valStop != 0 :
		x = x + 1
		
	else :
		y = y +1


#~ #####################################################################################################################

#~ #DECALAGE DE 1
print "\nphase 2"
x = 0
y = 0

while ( x < len(stop) and y < len(start) ) :

	valStop = stop[x] % 3
	valStart = start[y] % 3

	if  (valStart == 1 and valStop == 1) and (start[y] > stop[x]) :
		
		x = x + 1
		valStop = stop[x] % 3
		
		while  valStop != 1 :
			valStop = stop[x] % 3
			if valStop == 1 and start[y] < stop[x]:
				print "position start : " + str(start[y] + 1) + "\t position du codon stop : " + str(stop[x] + 3)
				break
				
			elif valStop == 1 and start[y] > stop[x]:
				break
				
			x = x + 1
	
	elif valStop != 1 :
		x = x + 1
		
	else :
		y = y +1

#~ #####################################################################################################################

#~ #DECALAGE DE 1
print "\nphase 3"
x = 0
y = 0

while ( x < len(stop) and y < len(start) ) :

	valStop = stop[x] % 3
	valStart = start[y] % 3

	if  (valStart == 2 and valStop == 2) and (start[y] > stop[x]) :
		
		x = x + 1
		valStop = stop[x] % 3
		
		while  valStop != 2 and x <= len(stop)-1:
			valStop = stop[x] % 3
			if valStop == 2 and start[y] < stop[x]:
				print "position start : " + str(start[y] + 1) + "\t position du codon stop : " + str(stop[x] + 3)
				break
				
			elif valStop == 2 and start[y] > stop[x]:
				break
				
			x = x + 1
	
	elif valStop != 2 :
		x = x + 1
		
	else :
		y = y +1
	
