def unicode(s):
    for c in s:
        result = ""
        
        print("point de code:", bin(ord(c))[2:])
        
        bins = bin(ord(c))[2:]
        bins = bins[::-1]
        
        if len(bins) <= 7:
            result += bins + "0"
            
        elif len(bins) >= 8 and len(bins) <= 11:
            result += bins[:6] + "01"
            result += bins[6:] + "0"*(5 - len(bins[6:])) + "011"

        elif len(bins) >= 12 and len(bins) <= 20:
            pass
        else:
            pass
        
        print("encodage utf-8", result[::-1])
        

unicode("é")