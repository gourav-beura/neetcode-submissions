class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        lookup = defaultdict(list)
        for word in strs:
            dat = [0]*26

            for ch in word.lower():
                if ord(ch)>=ord('a') and ord(ch)<=ord('z'):
                    dat[ord(ch)-ord('a')]+=1
            lookup[tuple(dat)].append(word)
        
        for key in lookup:
            result.append(lookup[key])
        
        return result

        