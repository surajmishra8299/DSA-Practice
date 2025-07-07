def unique(s):

    st = {} 
    vowel = 0
    conso = 0

    for ch in s:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            if ch not in st:
                st[ch] = True
                if ch in 'aeiouAEIOU':
                    vowel += 1
                else:
                    conso += 1

    print("Vowel:",vowel)
    print("Consonent:",conso)

chr = ("Hello World")
unique(chr)