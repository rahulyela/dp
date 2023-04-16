arr = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]
row=4
col=5
def kadane(arr):
    if(max(arr)<0):
        return max(arr)
    maxsum=-1e9
    curr=0
    for i in arr:
        curr+=i
        maxsum=max(maxsum,curr)
        if(curr<0):
            curr=0
    return maxsum
maxi=-1e9
for i in range(col):
    temp=[0]*row
    for j in range(i,col):
        for k in range(row):
            temp[k]+=arr[k][j]
        Sum=kadane(temp)
        maxi=max(maxi,Sum)
print(maxi)
#intunrion chechks for each column like 0-1,0-2,0-3,0-4,1-1,1-2----and apply kadine for ecah temp by adding to that
