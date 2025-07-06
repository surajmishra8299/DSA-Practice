'''

def removed(arr):

    remove = []
    
    for num in arr:
        if num not in remove:
            remove.append(num)
    return remove

num = [1,1,1,2,3,1,3,4,5,2]
print(removed(num))

'''

def remove_duplicates(arr):
    unique = [0] * len(arr)  # create list of same size
    index = 0

    for i in range(len(arr)):
        duplicate = False
        for j in range(index):
            if arr[i] == unique[j]:
                duplicate = True
                break

        if not duplicate:
            unique[index] = arr[i]
            index += 1

    # Only return the filled part (since rest is 0s)
    return unique[:index]

arr = [1, 1, 2, 3, 2, 4, 5, 3]
print(remove_duplicates(arr))