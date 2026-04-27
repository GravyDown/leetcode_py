class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st=set()

        i,j=0,k-1

        while j<len(s):
            substr=s[i:j+1]
            st.add(substr)
        
            i+=1
            j+=1
        
        if len(st)==2**k:
            return True
        else: return False
