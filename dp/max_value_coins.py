class Solution:
    def maxValueOfCoins(self, piles, k: int) -> int:
        def steps(i,k,piles,dp):
            # print(i,k)
            if(k==0):
                return 0
            if(i==len(piles)):
                return 0
            if(dp[i][k]!=-1):
                return dp[i][k]
            cost=0
            maxi=-1e9
            for j in range(0,min(k,len(piles[i]))):
                cost+=piles[i][j]
                take=cost+steps(i+1,k-j-1,piles,dp)
                maxi=max(maxi,take)
            ntake=steps(i+1,k,piles,dp)
            dp[i][k]=max(ntake,maxi)
            return max(ntake,maxi)
        dp=[[-1]*(k+1) for _ in range(len(piles))]
        return steps(0,k,piles,dp)
#new pattern we can take coins form a jar 0-len(jar) or we cannot take any value in that jar
class Solution:
    def maxValueOfCoins(self, piles, k: int) -> int:
        def steps(i,k,piles,dp):
            print(i,k)
            if(k==0):
                return 0
            if(i==len(piles)):
                return 0
            if(dp[i][k]!=-1):
                # print(i,k,"-----")
                return dp[i][k]
            take=-1e9
            if(len(piles[i])>0):
                cost=piles[i][0]
                piles[i].pop(0)
                take=cost+steps(i,k-1,piles,dp)
                piles[i].insert(0,cost)
            ntake=steps(i+1,k,piles,dp)
            dp[i][k]=max(take,ntake)
            return max(take,ntake)
        dp=[[-1]*(k+1) for _ in range(len(piles))]
        return steps(0,k,piles,dp)
#memorization fails XXXXX
#memorization works but TLE 108//124 beacoz we are not getting any subproblem any other value than j=0
#so instead of taking param we itrate over in eacg f call
class Solution:
    def maxValueOfCoins(self, piles, k: int) -> int:
        def steps(i,j,k,piles):
            # print(i,k,piles)
            if(k==0):
                return 0
            if(i==len(piles)):
                return 0
            if (i,j,k) in dict:
                return dict[(i,j,k)]
            take=-1e9
            if(j<len(piles[i])):
                take=piles[i][j]+steps(i,j+1,k-1,piles)
            ntake=steps(i+1,0,k,piles)
            dict[(i,j,k)]=max(take,ntake)
            return max(take,ntake)
        dict={}
        return steps(0,0,k,piles)
        