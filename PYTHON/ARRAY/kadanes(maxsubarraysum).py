def maxsubarray(arr):

    n = len(arr)
    curr_s=0
    max_s=arr[0]

    start = 0
    end = 0
    temp_s = 0

    for i in range(n):
        curr_s += arr[i]
    
        if curr_s > max_s:
            max_s = curr_s
            start = temp_s
            end = i
    
        if curr_s < 0:
            curr_s = 0
            temp_s = i+1

    return max_s, arr[start:end+1]

num = [1,-2,3,-6,7,4,-9,6,1,6,-1]
max_s, subarray = maxsubarray(num)

print("Maximum Sum:", max_s)
print("Subarray:", subarray)

# only maxsum

'''
def kadane(arr):
    curr_sum = 0
    max_sum = arr[0]

    for i in range(len(arr)):
        curr_sum = curr_sum + arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

    return max_sum

# Example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum is:", kadane(arr))

'''