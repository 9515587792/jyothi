xy,a=input().split()

xy,a=int(xy),int(a)

list=[int(b) for b in input().split()]

count=0

for i in range(0,xy):

      if a==list[i]:

           print("yes")

           break

      else:print("no")
