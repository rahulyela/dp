class Solution:
    def longestArithSeqLength(self, A) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        # return max(dp.values())
        A=[1,7,13,14,19]
        dp = [{} for _ in range(len(A))]
        maxi=0
        for i in range(1,len(A)):
            for j in range(i):
                diff=A[i]-A[j]
                if( diff in dp[j]):
                    dp[i][diff]=dp[j][diff]+1
                else:
                    dp[i][diff]=2
                maxi=max(dp[i][diff],maxi)
        print(dp)
        print(maxi)
#no of arthmetic subarrys
class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        return ans
#count all subsequne with len()>=3 artmetic

class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        n=len(nums)
        dp = [{}  for i in range(len(nums))]
        ans=0
        for i in range(1,n):
            for j in range(i):
                diff=nums[i]-nums[j]
                if(diff in dp[i]):
                    dp[i][diff]+=1
                else:
                    dp[i][diff] = 1
                if( diff in dp[j]):
                    dp[i][diff]+=dp[j][diff]
                    ans+=dp[j][diff]
                print(ans,"----")
        return ans           
            
            
        
        # def las(i,d,nums,temp,flag,dp,err):
        #     print(d)
        #     if(i==len(nums)):
        #         ans[0]=max(ans[0],len(temp))
        #         return 0
        #     t,nt=0,0
        #     if(flag ):
        #         if(d<0):
        #             x=test[0]+abs(d)
        #             if(dp[i][x]!=-1):
        #                 return dp[i][x]
        #         else:
        #             if(dp[i][d]!=-1):
        #                 return dp[i][d]
        #     else:
        #         if(dp[i][abs(d)]!=-1):
        #             return dp[i][abs(d)]
        #     if(len(temp)==0):
        #         t=1+las(i+1,d,nums,temp+[nums[i]],flag,dp,err)
        #         nt=las(i+1,err+1,nums,temp,flag,dp,err)
        #     if(len(temp)==1):
        #         t=1+las(i+1,nums[i]-temp[-1],nums,temp+[nums[i]],flag,dp,err)
        #         nt=las(i+1,err+1,nums,temp,flag,dp,err)
        #     if(len(temp)>=2):
        #         if(nums[i]-temp[-1]==d):
        #             t=1+las(i+1,nums[i]-temp[-1],nums,temp+[nums[i]],flag,dp,err)
        #         else:
        #             nt=las(i+1,d,nums,temp,flag,dp,err)
        #     if(flag):
        #         if(d<0):
        #             x=test[0]+abs(d)
        #             dp[i][x]=max(t,nt)
        #             print(temp,i,x)
        #         else:
        #             dp[i][d]=max(t,nt)
        #             print(temp,i,d)
        #     else:
        #         dp[i][abs(d)]=max(t,nt)
        #         print(temp,i,abs(d))
        #     return max(t,nt)
        # mini=float('inf')
        # maxi=float('-inf')
        # ans=[0]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         mini=min(mini,nums[j]-nums[i])
        #         maxi=max(maxi,nums[j]-nums[i])
        # test=[maxi,mini]
        # if((maxi>0 and mini>0) or (maxi<0 and mini<0)):
        #     flag=0
        # else:
        #     flag=1
        # err=abs(mini)+abs(maxi)+len(nums)+1
        # dp=[[-1]*(abs(mini)+abs(maxi)+len(nums)+3) for x in range(len(nums))]
        # print(len(dp[0]))
        # x=las(0,0,nums,[],flag,dp,err)
        # print(ans)
        # return ans[0]
       
                    
                
        