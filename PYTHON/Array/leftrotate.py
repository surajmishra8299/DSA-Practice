def left(arr):
    n = len(arr)
    start = arr[0]

    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=start

    return arr
num = [1,2,3,4,5,6]
print(left(num))    

# O/P = [2,3,4,5,6,1]