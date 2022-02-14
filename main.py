import sys

filesToRead = []
def readInputFile(inputFileName):
    with open(inputFileName) as inFile:
        for line in inFile:
            if line not in filesToRead:
                filesToRead.append(line.strip())

lines = []
def readFile(inFileName):
    with open(inFileName, encoding="utf-8") as inFile:
        for line in inFile:
            if line not in lines:
                lines.append(line)

def writeFile(filteredLines, outFileName):
    with open(outFileName, "w",  encoding="utf-8") as outFile:
        for line in filteredLines:
            outFile.write(line)

def FilterLines(inputFile, outputFileName):
    readInputFile(inputFile)
    for file in filesToRead:
        readFile(file)

    filteredLines = ""
    for line in lines:
        cols = line.split('\t')
        if line.startswith("DATE"): #Header
            filteredLines += line
            continue

        disease_trait = cols[7].lower()
        mapped_trait = cols[34].lower()
        p_val = cols[27].split("E")[1]

        traits = sys.argv[3:]
        for trait in traits:
            if (trait.lower() in disease_trait or trait.lower() in mapped_trait) and int(p_val) <= -8 and line not in filteredLines:
                filteredLines += line

    writeFile(filteredLines, outputFileName)

inputFile = sys.argv[1]
outputFileName = sys.argv[2]
FilterLines(inputFile, outputFileName)