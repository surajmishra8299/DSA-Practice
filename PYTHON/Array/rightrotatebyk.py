def rightbyk(arr,k):
    n = len(arr)
    k = k%n

    for _ in range(k):
        end = arr[-1]
        for i in range(n-2,-1,-1):
            arr[i+1] = arr[i]
        arr[0] = end

    return arr
num = [1,2,3,4,5,6]
print(rightbyk(num,2))

# O/P = [5,6,1,2,3,4]