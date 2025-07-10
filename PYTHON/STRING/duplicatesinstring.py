def duplicate(s):

    res = []
    frq = {}
    for ch in s:
        if ch in frq:
            frq[ch] += 1
        else:
            frq[ch] = 1

    for ch in frq:
        if frq[ch]>1:
            res.append(ch)
    return res

print(duplicate('HELLOJIKYAHAALHAI'))