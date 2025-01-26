class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countmapS = {}
        countmapT = {}

        if len(s) != len(t):
            return False
        
        for i in range (len(s)):
            countmapS[s[i]] = 1 + countmapS.get(s[i],0)
            countmapT[t[i]] = 1 + countmapT.get(t[i], 0)
        for j in countmapS : 
            if countmapS[j] != countmapT[j] :
                return False 
        return True
        
