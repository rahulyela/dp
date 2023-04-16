class Solution:
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        def breakegg(n,k,dp):
            if(k==0 or k==1):
                return k
            if(n==1):
                return k
            if(dp[n][k]!=-1):
                return dp[n][k]
            res=1e9
            for x in range(1,k+1):
                b=max(1+breakegg(n-1,x-1,dp),1+breakegg(n,k-x,dp))
                res=min(res,b)
            dp[n][k]=res
            return res
        dp=[[-1]*(k+1) for _ in range(n+1)]
        return(breakegg(n,k,dp)) 
#given kfloors and n eggs we have to minimize the trails to find floor where egg can be broken and egg canot
# be broken below them
# intutuion we try two cases in each and every floor break and nbreak 
#iterate x or 1,k+1
# if it breaks the floros above also be broken so reduces to k-x
# if not breaks the floors now becomes k-x 
#we take max beacoz we consider for the wrost cases and minize the all the wrost case
class Solution:
    def superEggDrop(self, egg: int, floor: int) -> int:
        def breakegg(egg,floor,dp):
            if(floor==0 or floor==1):
                return floor
            if(egg==1):
                return floor
            if(dp[egg][floor]!=-1):
                return dp[egg][floor]
            res=1e9
            low=1
            high=floor
            while(low<=high):
                mid=low+(high-low)//2
                left=1+breakegg(egg-1,mid-1,dp)
                right=1+breakegg(egg,floor-mid,dp)
                res=min(res,max(left,right))
                if(left<right):
                    low=mid+1
                else:
                    high=mid-1
            dp[egg][floor]=res
            return res
        dp=[[-1]*(floor+1) for _ in range(egg+1)]
        return(breakegg(egg,floor,dp)) 
#optimized e*f*log(f) instead of for loop we use binary search
