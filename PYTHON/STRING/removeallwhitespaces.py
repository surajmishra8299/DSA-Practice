def white(s):

    n = len(s)
    res = ''

    for ch in s:
        if ch != ' ':
            res = res + ch
    
    return res
    
print(white('I   AM SURAJ   '))