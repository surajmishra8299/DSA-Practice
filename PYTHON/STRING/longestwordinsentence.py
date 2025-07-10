def longestword(s):

    word = ''
    longest = ''

    for i in range(len(s)):
        if s[i] != ' ':
            word = word + s[i]
        
        else:
            if len(word)>len(longest):
                longest = word

            word = ''
    if len(word)>len(longest):
        longest = word

    return longest
print(longestword("My name is Suraj Mishra"))

'''

def longestword(s):
    words = s.split()
    longest = ''

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print(longestword("My name is Suraj Mishra"))


'''