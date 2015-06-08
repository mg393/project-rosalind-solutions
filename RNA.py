dna = ""
rna = ""

for nt in dna:
	if (nt == "A"):
		rna += "A"
	elif (nt == "G"):
		rna += "G"
	elif (nt == "T"):
		rna += "U"
	elif (nt == "C"):
		rna += "C"
	else:
		print("Nucleotide not recognised")
		break

print(rna)
