def subarray(arr,target):

    n = len(arr)
    start = 0
    curr_s = 0

    for end in range(n):
        curr_s += arr[end]

        while curr_s > target and start <= end:
            curr_s -= arr[start]
            start += 1

        if curr_s == target:
            print("Found",arr[start:end+1])
            return True

    print("No subarray")
    return False

num = [1,2,9,6,9,6,9]
print(subarray(num,12))