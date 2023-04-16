arr=[1,6,11,5]
target=sum(arr)//2
if(target==0):
    print("no")
else:
    if(target==0 and arr.count(0)>0):
        print(2**(arr.count(0)))
    dp=[[0]*(target+1) for x in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0]=1
    dp[0][arr[0]]=1
    for i in range(1,len(arr)):
        for k in range(0,target+1):
            take=0
            n_take=0
            take=dp[i-1][k]
            if(k-arr[i]>=0):
                n_take=dp[i-1][k-arr[i]]
            dp[i][k]=n_take+take
    print(dp[len(arr)-1][target])
    print(dp[-1])
    print("yes")
#inorder to find 2 subsets with abs(min diff)
# target=sum
# and check last row of dp and rerturn abs min value