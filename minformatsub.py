a1,b1=input().split()

a1,b1=int(a1),int(b1)

a2,b2=input().split()

a2,b2=int(a2),int(b2)

le1=(a1*60)+b1

le2=(a2*60)+b2

tmin=abs(le1-le2)

m=tmin%60

hrs=(tmin-m)//60

print(int(hrs),int(m))
