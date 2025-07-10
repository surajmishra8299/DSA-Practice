'''
def upperlower(s):

    n = len(s)
    print(s.upper(),s.lower())
 

upperlower('sUraj')

# without build in function

'''

'''
# Convert to uppercase
def up(s):

    res = ''
    for ch in s:
        if ('a' <= ch <= 'z'):
            res = res + chr(ord(ch)-32)
        else:
            res = res + ch
    return res

val = 'sUraj'
print(up(val))
 
'''

# Convert to lowercase
def lo(s):

    res = ''
    for ch in s:
        if ('A' <= ch <= 'Z'):
            res = res + chr(ord(ch)+32)
        else:
            res = res + ch
    return res

val = 'sUrAj'
print(lo(val))