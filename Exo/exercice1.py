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

# recherche du premier codon stop, recherche du start puis recherche condon stop

# PAS DE DECALAGE 
x = 0
y = 0

#for cmpt in range(0, len(stop)) :
while ( x <= len(stop) or y <= len(start) ) :

	valStop = stop[x] % 3
	valStart = start[y] % 3

	# pas de decalage 
	if  ( valStart == 0 and valStop == 0 ) and ( start[y] > stop[x] ) :
		x = x + 1
		print "test"
		while  valStop != 0 or len(stop) < x :
			valStop = stop[x] % 3
			
			if valStop == 0 :
				print "position start : " + str(start[y] + 1) + "\t position du codon stop : " + str(stop[x] + 1)
				break
				
			x = x + 1
	
	else :
		y = y + 1	


#~ #####################################################################################################################

#~ #DECALAGE DE 1
#~ cmpt = 0
#~ x = 0
#~ y = 0

#~ for cmpt in range(0, len(stop)) :
	
	#~ valStart = start[y] % 3
	#~ valStop = stop[x] % 3
		
	#~ # decalage de 1
	#~ if  ( valStart ==  1 and valStop == 1 ) and ( start[y] > stop[x] ) : 
		#~ while  valStop != 0 or len(stop) < x :
			#~ x = x + 1
			#~ valStop = stop[x] % 3
			
			#~ if valStop == 0 :
				#~ print "position start : " + str(start[y] + 1) + "\t position du codon stop : " + str(stop[x] + 1)
				#~ break
				
		#~ y = y + 1

#~ #####################################################################################################################

#~ #DECALAGE DE 1
#~ cmpt = 0
#~ x = 0
#~ y = 0

#~ for cmpt in range(0, len(stop)) :
	
	#~ valStart = start[y] % 3
	#~ valStop = stop[x] % 3
		
	#~ # decalage de 2 
	#~ if  ( valStart ==  2 and valStop == 2 ) and ( start[y] > stop[x] ) : 
		#~ while  valStop != 0 or len(stop) < x :
			#~ x = x + 1
			#~ valStop = stop[x] % 3
			
			#~ if valStop == 0 :
				#~ print "position start : " + str(start[y] + 1) + "\t position du codon stop : " + str(stop[x] + 1)
				#~ break
		
		#~ y = y + 1
		
	#~ y = y+1
	
	
#~ for cmpt in range(0,len(stop)):
	#~ valStart = start[i] % 3
	#~ valStop = stop[cmpt] % 3

	#~ if valStart == valStop :
		#~ print "position start : " + str(start[i]+1) + "\t position du codon stop : " + str(stop[cmpt]+1)
		#~ i = i+1
	
