class Solution:
    def numDecodings(self, s: str) -> int:
        if(s[0]=='0'):
            return 0
        if(s[len(s)-1]=='0' and (s[len(s)-2]=='0')):
            return 0
        if(s[len(s)-1]=='0' and int(s[len(s)-2])>2):
            return 0
        def decode(i,s):
            if(i>=len(s)):
                return 1
            if(s[i]=='0'):
                return 0
            t=0
            n=0
            x=0
            if(dp[i]!=-1):
                return dp[i]
            if(i+1<len(s) and s[i+1]=='0' and s[i]<'3'):
                x=decode(i+2,s)
            else:
                t=decode(i+1,s)
                if(i+1<len(s)):
                    if(s[i+1]<'7' and s[i]=='2'):
                        n=decode(i+2,s)
                    elif(s[i]<'2'):
                        n=decode(i+2,s) 
            dp[i]=n+t+x
            return n+t+x
        dp=[-1]*(len(s))
        x=decode(0,s) 
        return x
            
            