xy=input()

a=sum(c.isalpha() for c in xy)

b=sum(c.isdigit() for c in xy)

d=sum(c.isspace() for c in xy)

spsymbl=len(xy)-a-b-d

print(spsymbl)
