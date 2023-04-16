class Solution:
    def maxSumAfterPartitioning(self, arr, k: int) -> int:
        n=len(arr)
        def part(index,k,arr,dp):
            if(index==n):
                return 0
            if(dp[index]!=-1):
                return dp[index]
            length=0
            maxcurr=-1e9
            maxi=-1e9
            for i in range(index,min(index+k,n)):
                length+=1
                maxcurr=max(maxcurr,arr[i])
                Sum=length*maxcurr+part(i+1,k,arr,dp)
                maxi=max(maxi,Sum)
            dp[index]=maxi
            return maxi
        dp=[0]*(n+1)
        # return part(0,k,arr,dp)
#memoriztion intuntion is that we can part each array upto k elements and recervitly call index+1
        for index in range(n-1,-1,-1):
            length=0
            maxcurr=-1e9
            maxi=-1e9
            for i in range(index,min(index+k,n)):
                length+=1
                maxcurr=max(maxcurr,arr[i])
                Sum=length*maxcurr+dp[i+1]
                maxi=max(maxi,Sum)
            dp[index]=maxi
        return dp[0]
#tabulation-------------------------------



        