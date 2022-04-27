import re
import expressions as exp

def matchesStart(string, selectionList): #Only detects if the first characters matches the selection list
    for i, item in enumerate(selectionList):
        if(i > len(string)+1):
            continue
        if(not selectionList[i].matches(string[i])):
            return False
    return True

# \&$ 2&$


def getText(selectionString, textString, objectList):
    mostRecentObject = -10
    indexList = []
    selectionList = []
    # print("--------------------")
    index = -1 #budget for loop
    while(index < len(selectionString)-1): #Loop thorough selection and create a list of objects that makes comparisons easier
        index += 1

        # print(f"index: {index}, selectionString: {selectionString[index]}")

        if(re.match(r'&\$', selectionString[index:index+2])):
            # print("Found an object reference")
            if(selectionString[index-1] != '\\'):
                # print("Object reference is not escaped")
                # print(f"Detected object: |{selectionString[index:index+6]}|")
                selectionList.append(objectList[int(selectionString[index+3:index+6])])
                index += 5
                continue

        selectionList.append(exp.Literal(selectionString[index]))
    # print("--------------------")

    print(f"object list: {len(objectList)}")
    print(f"selection list:")
    for i in selectionList:
        print(f"|{i}|")
    #create a simple regex to match the selection string

    for stringIndex, i in enumerate(textString):
        if(matchesStart(textString[stringIndex:], selectionList)):
            print(list(range(stringIndex, stringIndex+len(selectionList))))
            indexList += list(range(stringIndex, stringIndex+len(selectionList)))
    return indexList   
# \&$ &$