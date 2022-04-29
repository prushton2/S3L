import expressions as exp

def matchesStart(string, selectionList): #Only detects if the first characters matches the selection list
    for i, item in enumerate(selectionList):
        if(i > len(string)-1):
            return False
        if(not selectionList[i].matches(string[i])):
            return False
    return True

def convertParseStringToList(parseString, objectList):

    selectionList = []

    i = -1
    while(i < len(parseString)-1):
        i += 1

        if(parseString[i] == "&" and parseString[i-1] != "\\"):
            listIndex = int(parseString[i+1:i+5])
            selectionList.append(objectList[listIndex])
            i += 4
        else:
            selectionList.append(exp.Literal(parseString[i]))

    return selectionList

def getMatchingIndices(whereString, fromString, objectList):
    
    selectionList = convertParseStringToList(whereString, objectList)


    matchingIndices = []
    for index, char in enumerate(fromString):
        if(matchesStart(fromString[index:], selectionList)):
            matchingIndices += (list(range(index, index+len(selectionList))))
    #removes duplicates
    matchingIndices = list(set(matchingIndices))
    matchingIndices.sort()

    return matchingIndices

def extendMatchingIndices(extensionArray, matchingIndices):
    #make it into a 2d array where i[x][0] is the start and i[x][1] is the end
    newMatchingIndices = []
    for index, item in enumerate(matchingIndices):
        if(index == 0):
            newMatchingIndices.append([item, None])
            continue
        if(item > matchingIndices[index-1]+1 and index != 0):
            newMatchingIndices[-1][1] = matchingIndices[index-1]
            newMatchingIndices.append([item, None])
            continue

    newMatchingIndices[-1][1] = matchingIndices[-1]

    matchingIndices = newMatchingIndices
    extendedSelection = []
    #extend the matching indices
    for index, item in enumerate(matchingIndices):
        leftBound = item[0] - extensionArray[0]
        rightBound = item[1] + extensionArray[3]

        innerLeftBound = rightBound if extensionArray[1] == -1 else item[0] + extensionArray[0]
        innerRightBound = leftBound if extensionArray[2] == -1 else item[1] - extensionArray[2]

        extendedSelection.append([leftBound, innerLeftBound])
        extendedSelection.append([innerRightBound, rightBound])


    print(f"matchingIndices: {matchingIndices}")
    return extendedSelection