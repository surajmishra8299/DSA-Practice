'''
def first(s):

    res = {}

    for ch in s:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            if ch in res:
                res[ch] += 1
            else:
                res[ch] = 1

    for ch in s:
        if ch in res and res[ch] == 1:
            return ch
    

    return None
print(first('aabbcddefghh'))
'''

def first(s):

    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
        if count == 1:
            return s[i]
    return None

print(first('aabcddefgg'))

