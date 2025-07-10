def rep(s,new,old):

    res = ''
    for ch in s:
        if ch == old:
            res = res + new
        else:
            res = res + ch
    return res

print(rep('suraj','L','s'))

