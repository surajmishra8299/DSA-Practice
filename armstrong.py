def Armstrong(n)

    sum=0
    count=0
    temp=n
    while temp!=0
        count+1
        temp = temp/10
    
    num = n
    while num!=0
        digit=num%10
        sum=sum+pow(digit,count)
        num=num/10

if n==sum
    print("Yes")
else
    print("Not")
