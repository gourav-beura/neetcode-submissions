class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        maxRight = [0]*len(height)
        minVal = [0]*len(height)
        result = [0]*len(height)

        for i in range(1,len(height)):
            maxLeft[i] = max(maxLeft[i-1],height[i-1])
        print(maxLeft)
        for i in range(len(height)-2,-1,-1):
            maxRight[i] = max(maxRight[i+1],height[i+1])
        print(maxRight)
        for i in range(len(height)):
            minVal[i] = min(maxLeft[i],maxRight[i])
        print(minVal)
        for i in range(len(height)):
            water_level = minVal[i] - height[i]
            if water_level > 0:
                result[i] = water_level
        
        return sum(result)
        