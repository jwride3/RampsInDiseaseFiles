import sys

lines = []

def readFile(inFileName):
    with open(inFileName) as inFile:
        for line in inFile:
            if line not in lines:
                lines.append(line)

def writeFile(filteredLines, outFileName):
    with open(outFileName, "w") as outFile:
        for line in filteredLines:
            outFile.write(line)

def FilterLines(numInputFiles, outputFileName):
    for i in range(numInputFiles):
        readFile(sys.argv[i + 3])
    filteredLines = ""

    for line in lines:
        cols = line.split('\t')
        if line.startswith("DATE"): #Header
            filteredLines += line
            continue

        disease_trait = cols[7].lower()
        mapped_trait = cols[34].lower()
        p_val = cols[27].split("E")[1]

        if ("hashimoto" in disease_trait or "hashimoto" in mapped_trait) and int(p_val) >= -8 and line not in filteredLines:
            filteredLines += line

    writeFile(filteredLines, outputFileName)

FilterLines(int(sys.argv[1]), sys.argv[2])