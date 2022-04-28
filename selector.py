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