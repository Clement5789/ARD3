def printASCII(s):
    result = []
    
    for l in s:
        result.append(hex(ord(l))[2:])
    
    return result
    
print(printASCII("'bonjour tout le monde!'\n\n'''programmer en\nPython'''"))