def count(arr):
    
     frq = {}
     for num in arr:
        if num in frq:
            frq[num] += 1
        else:
            frq[num] = 1
    
     for key in frq:
        print(key, "occurs", frq[key], "times")

num  = [12,336,56,12,69,336,336]
print(count(num))
