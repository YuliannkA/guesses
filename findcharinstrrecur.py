def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif char == aStr[int(len(aStr)/2)]:
        return True
    elif char > aStr[int(len(aStr)/2)]:
        return isIn(char, aStr[(int(len(aStr)/2)+1):])
    else:
        return isIn(char, aStr[:int(len(aStr)/2)])
