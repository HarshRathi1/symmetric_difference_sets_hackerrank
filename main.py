M=int(input())
a=set(map(int,input().split()))
N=int(input())
b=set(map(int,input().split()))
c=a.symmetric_difference(b)
c=sorted(list(c))
for i in c:
    print(i)