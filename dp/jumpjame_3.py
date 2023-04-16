def jump(arr,i,t):
        if(arr[i]==0):
            t[0]=1
            return 
        if(dp[i]!=0):
            return
        else:
            dp[i]=1
            if(i-arr[i]>=0 and dp[i-arr[i]]==0):
                jump(arr,i-arr[i],t)
            if(i+arr[i]<len(arr) and dp[i+arr[i]]==0):
                jump(arr,i+arr[i],t)
            return 
# start=2
arr=[]
t=[0]
dp=[0]*len(arr)
start=5
jump(arr,start,t)
print (bool(t[0]))
