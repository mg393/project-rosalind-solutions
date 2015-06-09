s1 = "<sequence 1>"
s2 = "<sequence 2>"

def hamm(sequence1, sequence2):
    result = 0
    i = 0

    sList2 = list(sequence2)
    for nt in sequence1:
        if(nt != str(sList2[i])):
            result += 1
        i += 1

    return result

print(hamm(s1, s2))
