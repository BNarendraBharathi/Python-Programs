for num in range(160):
    i=str(num)
    n=int(len(i))

    sum=0

    for number in range(n):
        modulo=int(i)%10

        sum=sum+((modulo**n))
        i=int(i)//10


    if sum==num:
        print(f"{num} is an armstrong number")



