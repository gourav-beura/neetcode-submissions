class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = set()

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in visited:
                visited.add(diff)
                visited.add(nums[i])
            else:
                j = nums.index(diff)
                if j < i:
                    return [j, i]
                else:
                    return [i,j]
        return []
        