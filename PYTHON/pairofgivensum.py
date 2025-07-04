def sum(arr,s):
    n = len(arr)
    for i in range(0,n):
        for j in range(1,n):
            if arr[i]+arr[j]==s:
                return {arr[i],arr[j]}
    return -1

num = [12,8,56,9,4,99]
print(sum(num,65))