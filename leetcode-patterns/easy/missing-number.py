# Problem:
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in
# the range that is missing from the array.

# Constraints:
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

# My Initial Solution:
#length = len(nums)
#dic = {}
#for i in range(length+1):
#    dic[i] = 0
#for num in nums:
#    if num in dic:
#        dic[num] = 1
#for key, value in dic.items():
#    if value == 0:
#        return key

# My Final Solution:
# The idea here is to XOR every number in two sets: the first set is the original array, the second
# set is the [0, n] array where n is the length of the original. When you XOR all of those values
# together, the remaining number actually turns out to be the missing number. This is because, for instance
# if you XOR 1 and 1, you get 0 because the binary values are the exact same (and XOR is 1 if bits are opposite).
# So when we go through and XOR all the numbers, the only remaining number will be the number that isn't
# in the original list because it's in the [0, n] set and when XORed with the original, it remains.

# Time Complexity and Space Complexity:
# The time complexity here is O(n) because we only loop through an array n times.
# The space complexity is O(1) because the amount of space required to calculate
# is constant. It doesn't grow with the size of the array, it will always be the same
# because we're not having to add in more numbers and take up more space.

# Other Solutions:
# 1) You can take the sum of the [0, n] list, and subtract that from the sum of the original list. The
# output actually turns out to be the missing number.


from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0 # Here we'll be XORing into
        # We want to loop len(nums)+1 so i goes from 0 to the largest number in nums
        for i in range(len(nums)+1):
            if i < len(nums): # Check to make sure we're not out of bounds, since i will be larger than the limit
                ans ^= nums[i] # XOR the current ans with whatever is in the array. Set ans equal to that.
            ans ^= i # XOR the current ans with whatever i is
            # The above operations work because XOR doesn't care what order you go in. Also repeats don't matter
            # either, cause they'll output 0 anyways. We also know there will only be one missing number, so we
            # don't  have to worry about accidentally adding in multiple numbers into ans
        return(ans)


class TestCase:
    def __init__(self, nums, expected_output):
        self.nums = nums
        self.expected_output = expected_output

def run_tests(solution, testcases):
    for case in testcases:
        if solution.missingNumber(case.nums) != case.expected_output:
            return False
    return True

solution = Solution()

a = TestCase([3,0,1], 2)
b = TestCase([0,1], 2)
c = TestCase([9,6,4,2,3,5,7,0,1], 8)
d = TestCase([1], 0)
e = TestCase([9, 8, 7, 6, 4, 1, 2, 3, 0], 5)

cases = [a, b, c, d]

print("TESTS PASSED" if run_tests(solution, cases) else "TEST FAILED")
