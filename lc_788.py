class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid=set([3,4,7])
        same=set([0,1,8])
        count=0

        for i in range(n+1):
            if i%10==i:
                if i not in invalid and i not in same:
                    count+=1
            
            else:
                num=i
                flag=False
                while num!=0:
                    d=num%10
                    if d in invalid:
                        flag=False
                        break
                    elif d in same:
                        num//=10
                        continue
                    else:
                        # count+=1
                        flag=True
                        num//=10
                if flag:
                    count+=1

        return count
                    
