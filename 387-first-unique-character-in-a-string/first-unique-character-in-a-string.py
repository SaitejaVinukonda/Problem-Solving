class Solution:
    def firstUniqChar(self, s: str) -> int:
        dici={}
        for i in range(len(s)):
            if s[i] in dici:
                dici[s[i]]+=1
            else:
                dici[s[i]]=1
        print(dici)        
        for i in dici:
            if dici[i]==1:
                return s.index(i)
        return -1