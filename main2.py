import sys
import os

lines = []
def readFile(inFileName):
    with open(inFileName) as inFile: #, encoding="utf-8"
        for line in inFile:
            if line not in lines:
                lines.append(line)

def writeFile(rsIDs, outFileName):
    with open(outFileName, "w") as outFile: #,  encoding="utf-8"
        for id in rsIDs:
            print(id)
            outFile.write(id + "\n")

def sortByCromosome(diseaseName):
    header = ""
    rsIDsMapped = {}
    for line in lines:
        cols = line.split('\t')
        if line.startswith("DATE"):  # Header
            header = line
            continue
        chromosome = cols[11]  # storing as an int or string?
        rsID = cols[21]
        if chromosome in rsIDsMapped:
            rsIDsMapped[chromosome].append(rsID)
        else:
            rsIDsMapped[chromosome] = [rsID]
    newFolder = diseaseName.strip() + "Chromosome"
    os.system("mkdir " + newFolder)
    for key in rsIDsMapped.keys():
        writeFileName = newFolder + "\\Chr" + key + ".txt"
        print (writeFileName)
        writeFile(rsIDsMapped[key], writeFileName)


inputFile = sys.argv[1]
readFile(inputFile)

sortByCromosome(sys.argv[2])
    #print(chromosome)

#for i in sorted (rsIDsMapped.keys()):
#    print(i + ": " + rsIDsMapped.values() )
#print(rsIDsMapped)