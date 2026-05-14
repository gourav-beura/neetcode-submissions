class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookUp = set(nums)
        res = 0
        for num in lookUp:
            if (num-1) not in lookUp:
                length=1
                while (num+length) in lookUp:
                    length+=1
                res = max(res,length)
        return res
        