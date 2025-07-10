def palindrome(arr):

    rev = 0
    num = arr

    while num != 0:
        digit = num%10
        rev = rev*10+digit
        num = num//10

    if arr == rev:
        print("Yes this is palindrome")
    else:
        print("No")

n = 121
palindrome(n)