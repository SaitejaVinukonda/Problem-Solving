class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        start=0
        for j in range(len(s)):
            if j==len(s)-1 or s[j]==" ":
                if j == len(s) - 1:
                    r=j
                else:
                    r=j - 1
                l = start
                while l<r:
                    s[l],s[r]=s[r],s[l]
                    l+=1
                    r-=1
                start=j+1
        return "".join(s)


