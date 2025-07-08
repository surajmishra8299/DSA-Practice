def palindrome(s):

     clean = ""
     for ch in s:
        if ch != ' ':
            clean = clean + ch.lower()
    
     n = len(clean)
     for i in range(n//2):
        if clean[i] != clean[n-i-1]:
            return "Not Palindrome"
     return "Palindrome"

print(palindrome("nurses run"))     # It is a Palindrome
print(palindrome("RaceCar"))        # It is a Palindrome
print(palindrome("Hello"))          # Not a Palindrome