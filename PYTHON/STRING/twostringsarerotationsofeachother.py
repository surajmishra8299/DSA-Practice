def rotate(s1, s2):

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        s1 = s1[1:] + s1[0]  # rotate left by 1
        if s1 == s2:
            return True

    return False

print(rotate('geeksforgeeks', 'geeksgeeksfor'))  # Output: 1