a,s=map(int,input().split())

count=0

for k in range(a,s):

     le=len(str(k))

     sum=0

     temp=k

     while k>0:

         a=k%10

         sum=sum+(a**le)

         k=k//10

     if(sum==temp):

         if(count==0):

                print(temp,end="")

         else:

             print("",end=" ")

             print(temp,end="")

         count=count+1
