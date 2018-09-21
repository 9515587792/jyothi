s=int(input())

list=[int(k) for k in input().split()]

list.sort()

print(" ".join(map(str,list)))
