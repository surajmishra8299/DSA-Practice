arr = [10,30,99,19,12,16]
min = arr[0]
max = arr[0]
for i in range(1,len(arr)):
    if min > arr[i]:
        min = arr[i]
    if max < arr[i]:
        max = arr[i]
print("MIN:",min)
print("MAX:",max)