import sys
def stable(strokes, holeindex, parscores, handicap):
    stablefordscore = 0
    i = 0
    minusx = int(handicap/18)
    minus1 = handicap%18
    for holestrokecount in strokes:
        if holestrokecount.isdigit():
            holestrokecount = int(holestrokecount)
            holeparscore = int(parscores[i])
            if int(holeindex[i]) <= minus1:
                scoretopar = holestrokecount - minus1 - 1 - holeparscore

            else:
                scoretopar = holestrokecount - minus1 - holeparscore
            if scoretopar > 1: #this was unde
                pass
            else:
                stablefordscore += abs(scoretopar - 2)
        elif holestrokecount == "X":
            pass
        else:
            stablefordscore = "Disqualified"
            break
        i += 1
    return stablefordscore

def getlongname(nameplayers):
    longname = 0
    for item in nameplayers:
        if len(item) > longname:
            longname = len(item)
    return longname


def getlongscore(stablescore):
    longscore = 0
    for score in stablescore:
        if len(str(score)) > longscore and score != "Disqualified":
            longscore = len(str(score))
    return longscore


def sorting(nameplayers,stablescore):
    i = 0
    while i < len(stablescore):
        p = i
        j = i + 1
        while j < len(stablescore):
            if str(stablescore[i]).isdigit() and str(stablescore[j]).isdigit() and p < len(stablescore):######2
                if stablescore[j] > stablescore[p]:
                    p = j
            j += 1
        temp = stablescore[p]
        stablescore[p] = stablescore[i]
        stablescore[i] = temp
        tempname = nameplayers[p]
        nameplayers[p] = nameplayers[i]
        nameplayers[i] = tempname
        i += 1
    orderednames = []
    orderedscores = []
    i = 0
    while i < len(stablescore):
        if stablescore[i] != "Disqualified":
            orderednames.append(nameplayers[i])
            orderedscores.append(stablescore[i])
        i += 1
    i = 0
    while i < len(stablescore):
        if stablescore[i] != "Disqualified":
            orderednames.append(nameplayers[i])
            orderedscores.append(stablescore[i])
        i += 1
    i = 0
    while i < len(stablescore):
        if stablescore[i] == "Disqualified":
            orderednames.append(nameplayers[i])
            orderedscores.append(stablescore[i])
        i += 1
    return orderednames, orderedscores

def printout(orderednames, orderedscores,lenname,lenscore):
    i = 0

    for i in range(0,len(orderednames)):
        print("{:>{}} : {:>{}}".format(orderednames[i],lenname,orderedscores[i],lenname))
    i += 1 ####1

def main():
    parscores = sys.stdin.readline().strip().split()
    holeindex = sys.stdin.readline().strip().split()
    nameplayers = []
    handicaps = []
    stablescore = []
    for line in sys.stdin:
        line = line.strip().split()
        nameplayers.append(" ".join(line[:-19]))
        handicap = int(line[-19])
        stablescore.append(stable(line[-18:], holeindex,parscores,handicap))
    lenname = getlongname(nameplayers)
    lenscore = getlongscore(stablescore)
    orderednames, orderedscores = sorting(nameplayers,stablescore)
    printout(orderednames, orderedscores, lenname, lenscore)

if __name__ == '__main__':
    main()