from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        maxS = nums[0]
        for n in nums:
            if s < 0:
                s = 0
            s += n
            maxS = max(s, maxS)
        return(maxS)

solution = Solution()

# Answer is 6
nums = [-2,1,-3,4,-1,2,1,-5,4]
solution.maxSubArray(nums)

# Answer is 1
nums = [1]
solution.maxSubArray(nums)

# Answer is 23
nums = [5,4,-1,7,8]
solution.maxSubArray(nums)
