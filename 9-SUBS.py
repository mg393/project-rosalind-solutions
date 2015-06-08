motif = "<motif here>"
cMotif = list(motif)
motifLength = len(cMotif)

dna = "<dna here>"
dnArray = list(dna)

locations = ""

position = 0

for nt in dnArray:
        if (nt == cMotif[0]):
                for x in range(0, (motifLength)):
                        if ((x + position) >= (len(dnArray))):
                                break
                        
                        if (dnArray[position + x] == cMotif[x]):
                                if (x >= (motifLength - 1)):
                                        locations += (str(position + 1) + " ")
                                        break 
                        else:
                                break
        position += 1

print(locations)
