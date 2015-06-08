dna = ""
A = 0
G = 0
C = 0
T = 0

for nt in dna:
	if (nt == "A"):
		A += 1
	elif (nt == "G"):
		G += 1
	elif (nt == "T"):
		T += 1
	elif (nt == "C"):
		C += 1
	else:
		print("Nucleotide not recognised")
		break

print("A = " + str(A) + ", C = " + str(C) + ", G = " + str(G) + ", T = " + str(T))
