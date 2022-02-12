#sort, reverse the list
#sorting
def sorting(list):
    list_length = range(len(list))
    for n in list_length:
        for m in range(len(list) - n - 1):
            if list[m] > list[m + 1]:
                list[m], list[m + 1] = list[m + 1], list[m]
        print(list)
    print(f"the sorted list:{list}")

#reversing the sorted list
def reverse(list):
    rlist = []
    length = len(list)

    for n in list:
        length = length - 1
        rlist.append(list[length])
        print(rlist)
    print(f"after reversing the sorted list:{rlist}")
numofelement =(input("enter the number of elements to  to be added in list:"))
list=numofelement.split()
print(list)

#calling the sorting function
sorting(list)
#calling the reverse function
reverse(list)
