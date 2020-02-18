list1 = ("ecky","abuu",1,2,3,4,5)
for num in list1:
    print(num)

temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("3 numbers  are palindrome!")
else:
    print("4  Not a palindrome!")

