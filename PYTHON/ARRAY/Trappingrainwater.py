def trapping(arr):

    n = len(arr)
    res = 0
    water = [0]*n

    for i in range(1,n-1):

        left = arr[i]
        for j in range(0,i):
            if left < arr[j]:
                left = arr[j]
        
        right = arr[i]
        for j in range(i+1,n):
            if right < arr[j]:
                right = arr[j]

        if left < right:
            res = res + left - arr[i]
            water[i] = left - arr[i]
        else:
            res = res + right - arr[i]
            water[i] = right - arr[i]

         
    print("Total Unit of Water:",res, "\nWater Pattern:",water)

num = [1,0,2,1,0,1,2,1,2,1]
trapping(num)