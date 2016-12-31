def readCsvFile(inPath,delim=' '):
    lst = []
    with open(inPath, 'r') as f:
        for line in f:
            fields = line.strip().split(delim)
            lst.append(fields)
    return lst