class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        cnt=0
        for i in s:
            if i =='(':
                if cnt>0:
                    stack.append(i)
                cnt+=1
            else:
                cnt-=1
                if cnt>0:
                    stack.append(i)
        return "".join(stack)