def second(arr):
    n = len(arr)

    first = second = -1
    for i in range(n):
        if first < arr[i]:
            second = first
            first = arr[i]
        elif arr[i]>second and arr[i]!=first:
            second = arr[i]
    
    return second

num = [16,5,96,4,95,65]
print(second(num))