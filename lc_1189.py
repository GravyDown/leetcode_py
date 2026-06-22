class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hsh={}
        count=0

        for c in text:
            if c in hsh:
                hsh[c]+=1
            else:
                hsh[c]=1

        flag=True
        while flag:
            
        
            for i in 'balloon':
                if i not in hsh or hsh[i]==0:
                    flag=False
                    break
                
                hsh[i]-=1
                
            if flag:
                count+=1
        
        return count
        
            
            
