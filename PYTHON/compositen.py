def composite(arr):
 
    res = []
    
    for num in arr:
        isC = False
        if num > 1:
            for j in range(2,num):
                if num%j==0:
                    isC = True
                    break

        if isC:
            res.append(num)
    return res
num1 = [1,2,3,4,5,6,7,8]
print(composite(num1))