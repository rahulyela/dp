class Solution:
	def findWinner(self, N,X,Y):
		# code here
            dp=[0]*(N+1)
            dp[1]=1
            for i in range(2,N+1):
                if(i-1>=0 and dp[i-1]!=1):
                    dp[i]=1
                elif(i-X>=0 and dp[i-X]!=1):
                    dp[i]=1
                elif(i-Y>=0 and dp[i-Y]!=1):
                    dp[i]=1
        # 	print(dp)
            return dp[N]

#steps to solve 1 person only wins if he losses at any n-1,n-x,n-y