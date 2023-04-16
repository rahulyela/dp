prev2=0
prev1=1
n=int(input())
for i in range(2,n+1):
    curr=prev2+prev1
    prev2=prev1
    prev1=curr
print(prev1)