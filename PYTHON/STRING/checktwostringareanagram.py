def anagram(s1,s2):

    if len(s1) != len(s2):
        return False

    count1 = [0]*26
    count2 = [0]*26

    for ch in s1:
        ch = ch.lower()
        if ('a' <= ch <= 'z'):
            count1[ord(ch)-ord('a')] += 1

    for ch in s2:
        ch = ch.lower()
        if ('a' <= ch <= 'z'):
            count2[ord(ch)-ord('a')] += 1

    return count1 == count2
      
    
print(anagram("Listen","Silent"))
print(anagram("Hello","World"))