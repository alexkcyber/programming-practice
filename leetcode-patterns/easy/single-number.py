# Problem:
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears only once.


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return(ans)

class TestCase:
    def __init__(self, nums, expected_output):
        self.nums = nums
        self.expected_output = expected_output

def run_tests(solution, testcases):
    for case in testcases:
        if solution.singleNumber(case.nums) != case.expected_output:
            return False
    return True

solution = Solution()

a = TestCase([2,2,1], 1)
b = TestCase([4,1,2,1,2], 4)
c = TestCase([1], 1)
d = TestCase([-1, -1, 2], 2)
e = TestCase([5], 5)
f = TestCase([1, 1], 0)

cases = [a, b, c, d, e]

print("TESTS PASSED" if run_tests(solution, cases) else "TEST FAILED")
