a=int(input(""))

rev=0

temp=a

while(a>0):

    val=a%10

    rev=rev*10+val

    a=a//10

if(temp==rev):

    print("yes")

else:

    print("no")
