import math
def ps(p,index,arr,target):
    if(target==0):
        return [p]
    if(index>=len(arr) or target<0):
        return []
    x=ps(p+[arr[index]],index,arr,target-(arr[index]*arr[index]))
    y=ps(p,index+1,arr,target)
    return x+y
target=int(input())
arr=[i for i in range(1,int(math.sqrt(target))+1)]
arr.reverse()
print(ps([],0,arr,target))