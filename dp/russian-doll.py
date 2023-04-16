import bisect
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        envelopes.sort(key=lambda x:x[1])
        def doll(i,prev,envelopes,dict):
            if(i>=len(envelopes)):
                return 0
            if((i,prev) in dict):
                return dict[(i,prev)]
            take=0
            if(prev==(-1,-1) or envelopes[i][0]>prev[0] and envelopes[i][1]>prev[1]):
                take=1+doll(i+1,(envelopes[i][0],envelopes[i][1]),envelopes,dict)
            ntake=doll(i+1,prev,envelopes,dict)
            dict[(i,prev)]= max(take,ntake)
            return max(take,ntake)
        dict={}
        return doll(0,(-1,-1),envelopes,dict)
#-------------------------------n*n time complexity -------------------------------
        dp=[]
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        for i in envelopes:
            x=bisect.bisect_left(dp,i[1])
            if(x==len(dp)):
                dp.append(i[1])
            else:
                dp[x]=i[1]
        return len(dp)
    #-----------------------------nlogn similar to lis but sorting is differnt -----------------------------