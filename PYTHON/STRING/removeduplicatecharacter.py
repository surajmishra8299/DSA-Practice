def duplicater(s):

    res = []
    for ch in s:
        if ch not in res:
            res.append(ch)

    return res

s1 = 'HELLOHLH'
print(duplicater(s1))