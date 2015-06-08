ssDNA = ""
cDNA = ""

for nt in ssDNA:
        if (nt == "T"):
            cDNA += "A"
        elif (nt == "A"):
            cDNA += "T"
        elif (nt == "G"):
            cDNA += "C"
        elif (nt == "C"):
            cDNA += "G"

cDNA = cDNA[::-1]
print(cDNA)
