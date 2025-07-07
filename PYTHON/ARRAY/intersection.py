def intersection(arr1,arr2):

    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = []
    
    for i in range(0,n1):
        for j in range(0,n2):
            if arr1[i] == arr2[j]:
                arr3.append(arr1[i])
                break
    return arr3

num1 = [1,2,3,4]
num2 = [1,6,3,9,2,5,3,4]

print(intersection(num1,num2))