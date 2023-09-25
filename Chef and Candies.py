t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    if n-c<=0:
        print(0)
    else:
        print((n-c+3)//4)
    
