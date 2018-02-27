def get_dna_complement(string):
	dna_complement = []

	for letter in dna string:
    	if letter == 'A':
        	dna_complement.append("T")
    	elif letter == 'T':
        	dna_complement.append('A')
    	elif letter == ('C'):
        	dna_complement.append('G')
    	elif letter == ('G'):
        	dna_complement.append('C')
    return ",".join(dna_complement)