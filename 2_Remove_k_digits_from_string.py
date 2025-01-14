
// Time Complexity  : O(n) 
// Space Complexity : O(n) 
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this    : No



class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        s=[]
        n=len(num)
        
        for i in range(0,n):
            while ( k>0 and len(s)>0 and s[-1] > num[i]):
                    s.pop()
                    k=k-1
            s.append(num[i]) 
                   
        while k>0:
            s.pop()
            k=k-1

        result=''.join(s)
        return (str(int(result))) if result else '0'