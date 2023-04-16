n=list(map(int,input().split()))
k=int(input())
dp=[0]*len(n)
for i in range(1,len(n)):
    m=float('inf')
    for j in range(1,k+1):
        if(i-j>=0):
            x=dp[i-j]+abs(n[i]-n[i-j])
            m=min(m,x)
    dp[i]=m
    print(dp)
print(dp[-1])

