# Problem:
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the
# integers in the range [1, n] that do not appear in nums.

# Constraints:
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n

from typing import List
from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic=Counter(nums) # This creates a dictionary with key: nums, and value: count of nums
        ans=[]
        for i in range(1, len(nums)+1): # We loop through
            if i not in dic: # If the number is not in the dic, we append. Return
                ans.append(i)
        return(ans)


class TestCase:
    def __init__(self, nums, expected_output):
        self.nums = nums
        self.expected_output = expected_output

def run_tests(solution, testcases):
    for case in testcases:
        if solution.findDisappearedNumbers(case.nums) != case.expected_output:
            return False
    return True

solution = Solution()

a = TestCase([4,3,2,7,8,2,3,1], [5,6])
b = TestCase([1,1], [2])
c = TestCase([1], [])
d = TestCase([1,2,3,4], [])
e = TestCase([2,1,3,7,9,8], [4,5,6])

cases = [a, b, c, d, e]

print("TESTS PASSED" if run_tests(solution, cases) else "TEST FAILED")
