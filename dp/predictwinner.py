def predict(score,arr,start,end,turn,player1,player2):
    if(start>end):
        return score
    x=predict(score+arr[start],arr[start+1:])
    y=predict(score+arr[end],arr[:end])
    if(turn&1==1):
        player1=max(x,y)
        return player1
    else:
        player2=max(x,y)
        return player2
arr=[1,2,5,3]

    
    

