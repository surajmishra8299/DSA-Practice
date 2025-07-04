def union(arr1,arr2):

    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = []
    for i in range(n1):
            if arr1[i] not in arr3:
                arr3.append(arr1[i])

    for j in range(n2):
        if arr2[j] not in arr3:
            arr3.append(arr2[j])
            
    return arr3

num1 = [1,3,6,8,9,6]
num2 = [1,6,7,4,8,6]

print(union(num1,num2))