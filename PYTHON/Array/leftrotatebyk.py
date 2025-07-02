def leftbyk(arr,k):
    n = len(arr)
    k = k%n      # for this mod use for the know about the range of the rotation

    for _ in range(k):
         start = arr[0]
         for i in range(1,n):
            arr[i-1]=arr[i]
         arr[n-1]=start

    return arr        
num = [1,2,3,4,5,6]
print(leftbyk(num,2))

# O/P = [3,4,5,6,1,2]