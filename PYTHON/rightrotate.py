def right(arr):
    n = len(arr)
    end = arr[-1]

    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=end
    
    return arr
num = [1,2,3,4,5,6]
print(right(num))

# O/P = [6,1,2,3,4,5]