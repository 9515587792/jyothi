ab=int(input())

if(ab<=1000):

    storage=input()

    storage=[int(y) for y in storage.split()]

    zz=sorted(storage[0:ab])

for i in range(0,ab):

     if(i<ab-1):

           g=' '

     else:

         g=''

     print(zz[i],end=g)
