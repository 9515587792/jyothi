ab,x=input().split()

ab,x=int(ab),int(x)

list=[int(k) for k in input().split()]

count=0

for i in range(0,ab):

      if x==list[i]:

        count+=1

print(count)
