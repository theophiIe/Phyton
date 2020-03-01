sequence = raw_input("la sequance : ")
sequence = sequence.upper()
sequenceTranscrit = ""

i = 0

while i < len(sequence) : 	
	if sequence[i] != "T" :
		sequenceTranscrit = sequenceTranscrit + sequence[i]
		
	elif(sequence[i] == "T") : 
		sequenceTranscrit = sequenceTranscrit + "U"
	
	i = i + 1
	
print ("La chaine transcrite est : ", sequenceTranscrit)
