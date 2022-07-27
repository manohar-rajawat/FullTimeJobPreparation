from collections import Counter
def familyCount(array):
    count = 0
    array = Counter(array)
    visited = {}
    for string in array.keys():
        if string in visited:
            count += visited[string]
        else:
            nextStringValue = nextString(string)
            if nextStringValue in array:
                count += array[nextStringValue]
                visited[string]=array[nextStringValue]
            else:
                visited[string]=0
    return count
            
    
def nextString(string):
    returnString = ""
    for char in string:
        returnString += chr((ord(char)+1-97)%26+97)
    return returnString

print (familyCount(['bag','sfe','cbh','cbh','red']))
