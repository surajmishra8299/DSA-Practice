def sort(arr):

    n = len(arr)
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            return "Not sorted"
    return "Sorted"

num = [1,2,5,1]
print(sort(num))
