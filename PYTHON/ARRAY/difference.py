def diff(arr1,arr2):

    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = []
    for i in range(0,n1):
        for j in range(0,n2):
            if arr1[i] == arr2[j]:
                break
        else:
            arr3.append(arr1[i])

    return arr3
num1 = [1,2,3,4,8,7]
num2 = [1,6,3,9,2,5,3,4]

print(diff(num1,num2))