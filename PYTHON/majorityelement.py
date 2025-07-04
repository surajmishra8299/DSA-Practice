def majority(arr):

    n = len(arr)
    for val in arr:
        frq = 0
        for el in arr:
            if el == val:
                frq += 1

        if frq >= n//2:
            return val

    return -1

num = [1,2,2,2,2,3,6,8,9]
print(majority(num))