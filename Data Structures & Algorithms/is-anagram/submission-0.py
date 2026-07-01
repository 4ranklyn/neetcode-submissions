class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        counts=[0] * 26

        for a in s:
            i=ord(a)-ord('a')
            counts[i]+=1
        for b in t:
            i=ord(b)-ord('a')
            counts[i]-=1
        
        if all(count == 0 for count in counts):
            return True
        else:
            return False 


