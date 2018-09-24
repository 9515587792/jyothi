xy=int(input())

s=[]

rev1=0

count=0

while xy>0:

    temp=xy%10

    rev1=rev1*10+temp

    xy=xy//10

    count+=1

while rev1>0:

    temp=rev1%10

    s.append(temp)

    rev1=rev1//10

for i in range(0,count):

    if i<count-1:

        g=' '

    else:

        g=''

    print(s[i],g)
