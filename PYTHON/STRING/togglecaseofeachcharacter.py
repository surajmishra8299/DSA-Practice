def toggle(s):

    res = ''
    for ch in s:
        if 'a' <= ch <= 'z':
           res = res + chr(ord(ch)-32)

        elif 'A' <= ch <= 'Z':
            res = res + chr(ord(ch)+32)

        else:
            res = res + ch

    return res
print(toggle('pYtHOn123'))