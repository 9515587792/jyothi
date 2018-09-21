n=int(input())

num=n

sum=0

while(n>0):

           a=n%10

           sum=sum+a**3

           n=n//10

if(num==sum):

            print("yes")

else:

            print("no")
