import functools
class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=len)
        dp=[1]*(len(words))
        # print(words)
        def combine(s1,s2):
            if(len(s1)+1!=len(s2)):
                return False
            i=0
            j=0
            count=0
            while(i<len(s1)):
                if(s1[i]==s2[j] and j<len(s2)):
                    i+=1
                    j+=1
                else:
                    j+=1
                    count+=1
                    if(count>1):
                        return False
            return True
        for i in range(len(words)):
            for j in range(i):
                if(combine(words[j],words[i])):
                    dp[i]=max(dp[i],dp[j]+1)
        # print(dp)
        return max(dp)
#---------------------------o(n*2)*l--------------------------
class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=len)
        dict={word:1 for word in words}
        # print(words)
        for word in words:
            curr=1
            for j in range(len(word)):
                pre=word[:j]+word[j+1:]
                if( pre in dict):
                    curr=max(curr,dict[pre]+1)
            dict[word]=curr
        # print(dp)
        return max(dict.values())
    #------------n*n------------------------optimized-------