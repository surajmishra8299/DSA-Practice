def frq(s):

    res = {}
    for ch in s:
        if ch in res:
            res[ch] += 1
        else:
            res[ch] = 1

    return res

print(frq('BANANA'))