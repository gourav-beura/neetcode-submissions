class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookUp = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target-num
            if diff in lookUp:
                return [lookUp[diff],i]
            lookUp[num] = i 

            

        