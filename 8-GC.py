from sys import argv

scriptname, file = argv
filedata = open(file).read()

def parseData(data): #objective is to return a dictionary of file and list of IDs
    resultdict = {}
    tempdict = {}
    lastID = ""
    listofIDs = []
    for line in data.splitlines():
        if (line.startswith(">")): #line is ID
            lastID = line[1:]
            tempdict = { line[1:]:None }
            resultdict.update(tempdict)
            listofIDs.append(lastID)
        else:
            resultdict[lastID] = line

    return resultdict, listofIDs

def calcGC(dictionary, idlist):
    highestID = ""
    highestGC = 0

    for entry in idlist:
        GC = 0.0
        total = 0.0
        percentGC = 0.0
        for nt in dictionary[entry]:
            if (nt == "C" or nt == "G"):
                GC += 1.0
                total += 1.0
            else:
                total += 1.0

        percentGC = (GC/total)*100

        if (percentGC > highestGC):
            highestGC = percentGC
            highestID = entry

    return highestID, highestGC

dict, listIDs = parseData(filedata)
seqID, seqGC = calcGC(dict, listIDs)
print(seqID)
print(seqGC)
