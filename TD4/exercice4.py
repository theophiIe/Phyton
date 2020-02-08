sequence = raw_input("la sequance : ")
inver = ""
i = len(sequence)

while i != 0:
	inver = inver + sequence[i-1]
	i = i-1

if inver == sequence : 
	print "c'est un palindrome"

else :
	print "ce n'est pas un palindrome"
	
