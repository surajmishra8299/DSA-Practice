def reverse(s):

    n = len(s)
    rev = ' '

    for i in range(n-1,-1,-1):
        rev = rev + s[i]

    return rev

arr = ('SURAJ')
print(reverse(arr))