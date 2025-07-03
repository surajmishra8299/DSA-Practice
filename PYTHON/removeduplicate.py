def removed(arr):

    remove = []
    for num in arr:
        if num not in remove:
            remove.append(num)
    return remove

num = [1,1,1,2,3,1,3,4,5,2]
print(removed(num))