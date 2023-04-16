class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        def lcs(i,j,k,A,B,C,dp):
            if(i>=len(A) or j>=len(B) or k>=len(C)):
                return 0
            if(dp[i][j][k]!=-1):
                return dp[i][j][k]
            if(A[i]==B[j] and A[i]==C[k]):
                x=1+lcs(i+1,j+1,k+1,A,B,C,dp)
                dp[i][j][k]=x
                return x
            elif(A[i]!=B[j] or B[j]!=C[k] or C[k]!=A[i]):
                t1=lcs(i+1,j,k,A,B,C,dp)
                t2=lcs(i,j+1,k,A,B,C,dp)
                t3=lcs(i,j,k+1,A,B,C,dp)
                dp[i][j][k]=max(t1,t2,t3)
                return max(t1,t2,t3)
        dp=[[[-1]*(len(C)) for _ in range(len(B))] for _ in range(len(A))]
        return lcs(0,0,0,A,B,C,dp)
                
#-----------------similar to lcs of 2 but if not match then increse +1 of s1 or +1 of s2 or +1 of s3 and 
#--and rreturn max(all)--------------------