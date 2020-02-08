sequence = raw_input("la sequance : ")
brinCmpl = ""
inver = ""
i = len(sequence)

while i != 0:
	if sequence[i-1] == "A":
		brinCmpl = brinCmpl + "T"
		
	if sequence[i-1] == "T":
		brinCmpl = brinCmpl + "A"
		
	if sequence[i-1] == "C":
		brinCmpl = brinCmpl + "G"
		
	if sequence[i-1] == "G":
		brinCmpl = brinCmpl + "C"
	
	i = i-1

print brinCmpl

i = 0

while i<len(brinCmpl) : 
	inver = inver + brinCmpl[i]
	i = i+1
	
if inver == sequence :
	print "C'est un palindrome"
	
else :
	print "N'est pas un palindrome"
