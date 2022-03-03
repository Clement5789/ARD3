def rot13(s):
    caracters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ '
    result = ""
    
    for l in s:
        pos = caracters.index(l)
        pos += 13
        pos %= len(caracters) - 1
        result = result + caracters[pos]
        
    return result

print(rot13("Python"))
        