print("Enter lists with Negative numbers\n")
lists = [int(x) for x in input().split()]
listNegative =[]
negLocation =[]
print(lists)
for i in lists:
    if(i<0):
        listNegative.append(i)
        negLocation.append(lists.index(i))
if (len(listNegative)==0):
    print("Sorry No negative number detected!")
else:
    print("Negative numbers in lists are:- \n ",listNegative)
    print("location of negative elements are ", negLocation)
