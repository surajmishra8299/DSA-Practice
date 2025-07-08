def sent(s):


    ch = s.split()
    rev = []
    for word in ch:
        rev.append(word[::-1])
    
    print(' '.join(rev))
words = 'My Name is Suraj'

sent(words)