#printing stars in hollow right triangle shape
row = int(input ("enter the number of row : "))
for i in range(row):
    for j in range(i+1):
        if i==row-1 :
            print("*",end="")
        elif j==0 or j==i:
            print("*",end="")

        else:
            print(" ",end="")    
    print("\n") 