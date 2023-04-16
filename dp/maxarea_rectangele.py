#---------------in histogram---------------------------------------------
class Solution:
    def largestRectangleArea(self, hist) -> int:
        left=[-1]*(len(hist))
        right=[-1]*(len(hist))
        stack=[]
        n=len(hist)
        for i in  range(len(hist)):
            if(stack==[]):
                left[i]=0
                stack.append(i)
            else:
                while(stack!=[] and hist[stack[-1]]>=hist[i]):
                    stack.pop()
                if(stack==[]):
                    left[i]=0
                else:
                    left[i]=stack[-1]+1
                stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            if(stack==[]):
                right[i]=n-1
                stack.append(i)
            else:
                while(stack!=[] and hist[stack[-1]]>=hist[i]):
                    stack.pop()
                if(stack==[]):
                    right[i]=n-1
                else:
                    right[i]=stack[-1]-1
                stack.append(i)
        # print(left,right)
        maxarea=0
        for i in range(n):
            width=(right[i]-1)-(left[i]+1)+1
            area=hist[i]*width
            # print(area)
            maxarea=max(maxarea,area)
        return(maxarea)
#-------------in grid----------------------------------------------------------------------------------
# intutuion is similar but we find raectangle area straing from  row and add to next row
class Solution:
    def maximalRectangle(self, matrix) -> int:
        def area(hist):
            left=[-1]*(len(hist))
            right=[-1]*(len(hist))
            stack=[]
            n=len(hist)
            for i in  range(len(hist)):
                if(stack==[]):
                    left[i]=0
                    stack.append(i)
                else:
                    while(stack!=[] and hist[stack[-1]]>=hist[i]):
                        stack.pop()
                    if(stack==[]):
                        left[i]=0
                    else:
                        left[i]=stack[-1]+1
                    stack.append(i)
            stack=[]
            for i in range(n-1,-1,-1):
                if(stack==[]):
                    right[i]=n-1
                    stack.append(i)
                else:
                    while(stack!=[] and hist[stack[-1]]>=hist[i]):
                        stack.pop()
                    if(stack==[]):
                        right[i]=n-1
                    else:
                        right[i]=stack[-1]-1
                    stack.append(i)
            # print(left,right)
            maxarea=0
            for i in range(n):
                width=(right[i])-(left[i])+1
                area=hist[i]*width
                # print(area)
                maxarea=max(maxarea,area)
            return(maxarea)
        n=len(matrix)
        m=len(matrix[0])
        heights=[0]*(m)
        sol=0
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]=="1"):
                    heights[j]+=1
                else:
                    heights[j]=0
            t=area(heights)
            sol=max(sol,t)
        return sol
        
        
        
        
        
        
        
        
        
        
        

        