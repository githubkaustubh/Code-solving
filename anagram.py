class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count1 = {}
        count2 = {}

        if len(s) != len(t):
            return False
        
        for i in range (len(s)):
            count1[s[i]] +  = count1[s[i]]
            count2[t[i]] + =  count2[t[i]]
        for j in count2 : 
            if count1[j] != count2[j]
            return False 
        return True
