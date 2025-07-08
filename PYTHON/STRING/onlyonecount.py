def one(s,c):

    count = 0

    for ch in s:
            if ch == c:
                count += 1
            
    return count

oneC = ('Hello World')
letter = 'l'
print(one(oneC,letter))
