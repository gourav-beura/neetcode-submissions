class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dat = [0]*26

        for ch in s.lower():
            s_dat[ord(ch)-ord('a')]+=1
        
        t_dat = [0]*26
        for ch in t.lower():
            t_dat[ord(ch)-ord('a')]+=1
        
        return s_dat==t_dat
        