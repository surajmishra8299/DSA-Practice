def movezero(arr):
    
    move = []
    
    for i in arr:
        if i != 0:
            move.append(i)
    for i in arr:
        if i == 0:
            move.append(i)

    return move
        

num = [0,0,0,9,0,7,0,0,5,1]
print(movezero(num))
       

