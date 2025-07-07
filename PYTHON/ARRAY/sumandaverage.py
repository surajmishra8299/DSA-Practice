arr = [10,20,30,40]
sum = 0
avg = 0

for i in range(0,len(arr)):
    sum = sum+arr[i]
    avg = sum/len(arr)
print(sum)
print(avg)