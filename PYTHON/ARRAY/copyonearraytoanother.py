def copyanother(arr1):
    n = len(arr1)
    arr2 = []

    for i in range(n):
        arr2.append(arr1[i])
    return arr2
arr3 = [10,20,30,40]
print(copyanother(arr3))

# O/P = [10,20,30,40]