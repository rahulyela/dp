class Solution:
    def partition(self, s: str):
        n=len(s)
        def part(index,temp,s):
            # nonlocal ans
            if(index==n):
                ans.append(temp)
                return
            for i in range(index,n):
                if s[index:i+1]== s[index:i+1][::-1]:
                    t=s[index:i+1]
                    part(i+1,temp+[t],s)
            return
        ans=[]
        part(0,[],s)
        return(ans)
#print all partion such that evry substring is palinfrome
#intution iterte over index and check if ist is palindrome then make  a cut else continue
class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        def ispalindrome(t):
            if(t==t[::-1]):
                return True
            else:
                return False
        def part(index,s,dp):
            if(index==n):
                return 0
            if(dp[index]!=-1):
                return dp[index]
            mini=float('inf')
            temp=''
            for i in range(index,n):
                temp+=s[i]
                if(ispalindrome(temp)):
                    cost=1+part(i+1,s,dp)
                    mini=min(mini,cost)
            dp[index]=mini
            return mini
        dp=[-1]*(n)
        return part(0,s,dp)-1
#partion into min such that evry substring is palindrom        
#similar to that but each iteration we carry mini cuts