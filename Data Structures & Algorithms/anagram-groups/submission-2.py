class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        lookUp = defaultdict(list)


        for s in strs:
            dat = [0]*26
            s = s.lower()
            for ch in s:
                dat[ord(ch)-ord('a')]+=1
            lookUp[tuple(dat)].append(s)
        
        for dat in lookUp:
            res.append(lookUp[dat])
        
        return res
        

        