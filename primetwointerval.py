n1=int(input())

n2=int(input())

count=0

for k in range(n1+1,n2,1):

          for i in range(2,k,1):

                        if(k%i==0):

                                    count=count+1

                        if(count==0):

                                     print(k)
