def jump(arr,i,sol):
    if(i==len(arr)):
        # print(sol[-1])
        return sol[-1]
    x=sol[i-1]+abs(arr[i-1]-arr[i])
    y=float('inf')
    if(i-2>=0):
        y=sol[i-2]+abs(arr[i-2]-arr[i])
    sol[i]=min(x,y)
    ans=jump(arr,i+1,sol)
    return ans
arr=list(map(int,input().split()))
sol=[-1]*(len(arr))
sol[0]=0
print(jump(arr,1,sol))
print(sol)


