def arrange(arr):

    n = len(arr)
    s = 0
    e = n-1
    while(s<e):
            if arr[s] >= 0:
                s += 1

            elif arr[e] < 0:
                e -= 1

            else:
                arr[s] , arr[e] = arr[e] , arr[s]
                s += 1
                e -= 1
    return arr

num = [-1,-2,3,4,-6,7]
print(arrange(num))