from typing import List


from typing import List


class Solution:
    def sumZeroMatrix(self, a) -> List[List[int]]:
        # code here
        row=len(a)
        col=len(a[0])
        def presum(arr,up,down):
            # print(arr)
            hash={}
            SUM=0
            max_lenght=0
            ans=False
            for j,i in enumerate(arr):
                SUM+=i
                if(i==0):
                    if(1>max_lenght):
                        max_lenght=1
                        up=j
                        down=j
                        ans=True
                if(SUM==0):
                    if(j+1>max_lenght):
                        max_lenght=j+1
                        up=0
                        down=j
                        ans=True
                if(SUM in hash):
                    # print(j-(hash[SUM]),max_lenght,"oo")
                    if(j-(hash[SUM])>max_lenght):
                        max_lenght=j-(hash[SUM])
                        up=(hash[SUM]+1)
                        down=j
                        ans=True
                else:
                    hash[SUM]=j
                # print(max_lenght,up,down,SUM,hash)
            return ans,up,down
        maxi=-1e9
        lu,ld,l,r=0,0,0,0
        for i in range(col):
            temp=[0]*row
            for j in range(i,col):
                for k in range(row):
                    temp[k]+=a[k][j]
                up,down=0,0
                ans,up,down=presum(temp,up,down)
                # print(ans,'$$$$')
                if(ans):
                    area=(down - up + 1) * (j - i + 1)
                    # print(area,up,down,i,j,'---------')
                    if(area>maxi):
                        maxi=area
                        lu=up
                        ld=down
                        l=i
                        r=j
        # print(lu,ld,l,r)
        if(maxi==-1e9):
            return [[-1]]
        sol=[]
        for i in range(lu,ld+1):
            t=[]
            for  j in range(l,r+1):
                t.append(a[i][j])
            sol+=[t]
        return(sol)       
#intuition simiar to maxi 2d sum but we use prefix sum and caluclaute boundarys 