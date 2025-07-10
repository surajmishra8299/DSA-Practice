def count(s):

    vowel = 0
    conso = 0

    for ch in s:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            if ch in 'aeiouAEIOU':
                vowel += 1
            else:
                conso += 1

    print("Vowel:",vowel)
    print("Consonent:",conso)

chra = ("Hello World")
count(chra)