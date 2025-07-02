def search(arr,ele):

    n = len(arr)
    for i in range(0,n):
        if arr[i] == ele:
            return "Yes"
    return "No"
num = [15,89,59,68,53,76]
print(search(num,59))