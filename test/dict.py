def putInfoToDict(fileName):
    checkintimeList = list()
    sNoDict = {}
    with open(fileName,'r') as rFile:
        lines = rFile.read().replace(',\n','').replace(';','').split('\t')
        for line in lines:
            temp = line.replace('(','').strip().split(',')[0].strip()
            lessonid = line.split(',')[1].replace(')','').strip()
            sNo = int(line.split(',')[2].replace(')','').strip())
            checkintime = temp[1:-1]
            checkintimeDict = {'lessonid': lessonid, 'checkintime': checkintime}
            if sNo not in sNoDict:
                sNoDict[sNo] = []
                sNoDict[sNo].append(checkintimeDict)
            else:
                sNoDict[sNo].append(checkintimeDict)
        return (sNoDict)

fileName = 'E:\\0005_1.txt'
print(putInfoToDict(fileName))
