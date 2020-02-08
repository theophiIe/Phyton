sequence = raw_input("la sequance : ")
brinCmpl = ""
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
