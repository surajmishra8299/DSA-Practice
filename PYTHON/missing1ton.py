def missing(arr,r):

    miss = []
    
    for i in range(1,r+1):
        if i not in arr:
            miss.append(i)
    return miss

num = [1,2,4,6,9,10,11,13,16]
print(missing(num,16))