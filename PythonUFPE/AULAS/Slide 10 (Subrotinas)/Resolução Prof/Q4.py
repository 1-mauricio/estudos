def anagrama(p1, p2):
    if len(p1) != len(p2):
        return False

    d = {}
    for p in p1:
        p = p.lower()
        if p not in d:
            d[p] = 1
        else:
            d[p] += 1

    i = 0
    anag = True
    while i < len(p2) and anag:
        aux = p2[i].lower()
        if (aux in d) and (d[aux] > 0):
            d[aux] -= 1
        else:
            anag = False
        i += 1

    return anag


# True
palavra1 = "abcde"
palavra2 = "Eabcd"
print(anagrama(palavra1, palavra2))

# True
palavra1 = "abCde"
palavra2 = "EabcD"
print(anagrama(palavra1, palavra2))

# False
palavra1 = "abcde"
palavra2 = "abcd"
print(anagrama(palavra1, palavra2))

# False
palavra1 = "abcd"
palavra2 = "abcde"
print(anagrama(palavra1, palavra2))

# False
palavra1 = "abcd"
palavra2 = "aabc"
print(anagrama(palavra1, palavra2))

# False
palavra1 = "aabc"
palavra2 = "abcc"
print(anagrama(palavra1, palavra2))