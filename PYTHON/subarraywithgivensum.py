def subarray(arr):

    n = len(arr)
    start = 0
    curr_s = 0

    for end in range(n):
        curr_s += arr[end]

        while curr