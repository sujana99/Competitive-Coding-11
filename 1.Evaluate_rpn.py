
// Time Complexity  : O(n) 
// Space Complexity : O(k) k=number of intergers
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this    : No

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        
        for i in tokens:
            if i in ['+','*','-','/']:
                b=stack.pop()
                a=stack.pop()
                # print(a,b,i)
                if i== '+':
                    stack.append(a+b)
                elif i== '-':
                    stack.append(a-b)
                elif i== '*':
                    stack.append(a*b)
                elif i== '/':
                    stack.append(int(a/b))
            else:
                stack.append(int(i))
                    
        return stack[0]