class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lookUp = Counter(nums)
        for num in lookUp:
            if num == val:
                for i in range(lookUp[num]):
                    nums.remove(num)
        return len(nums)
        