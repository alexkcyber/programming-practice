# Problem:
# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is
# distinct.

# Constraints:
# 1 <= nums.length <= 105
# -10^9 <= nums[i] <= 10^9

# My Approach:
# Loop through the array, placing each item into a dictionary. The
# moment we hit a duplicate value in the dictionary, we return true. If
# we hit the end of the array, we return false. The reason this is a valid
# solution is because dictionaries can only have unique 'key' values. So when
# we add a new key, we first have to check if it already exists. If so, then
# we know that the array contains a duplicate value. If we loop through the
# whole array and finish adding all the numbers into the dictionary as keys,
# we know that the array does not contain duplicates.

# Time Complexity and Space Complexity:
# Because we only loop through the array once, time complexity is O(n). Since
# we are adding the numbers into a dictionary, space complexity is also O(n).
# This is because we have to add n elements (the number of elements in the array)
# into a hashmap, thus taking up more space.

# Other Solutions:
# 1) Create a set of the original array. Sets cannot have any duplicate values.
# Then you can check the length of the new set and compare it to the array. If
# they differ, then the array contained duplicate values
# 2) Obvious brute forcing. Just check every value. n^2 time complexity

from typing import List # Need this import to use 'List'

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {} # We start by creating a dictionary
        for num in nums: # Loop through the numbers
            if num not in dict: # If the number isn't in the dictionary, add it
                dict[num] = num # Key must be unique, but value can be anything. So set it as the same
            else:
                return True # If num exists in the dict, then we found a duplicate. Return True
        return False # If we finish adding values to the dict, we return False. All values unique

class TestCase:
    # This class allows us to define a test case

    def __init__(self, nums, result):
        '''
        Initialize the object

        nums: an array of numbers to test
        result: what the expected outcome should be
        '''

        self.nums = nums
        self.result = result

def test_cases(solution, cases):
    '''
    test_cases takes all of our cases and tests to make sure they pass

    solution: our solution class. This is just a leetcode thing, have to pass it in.
    cases: an array of TestCase objects
    '''

    for case in cases: # Loop through all of the cases in our cases array
        # If the return value of the function doesn't equal what we are expecting, return False
        if solution.containsDuplicate(case.nums) !=  case.result:
            return False
    return True # If we loop all the way through and all pass, then we return True

# Here is how we call the containsDuplicate function
solution = Solution()

# We define our test cases
a = TestCase([1,2,3,1], True)
b = TestCase([1,2,3,4], False)
c = TestCase([1,1,1,3,3,4,3,2,4,2], True)
d = TestCase([5], False)
e = TestCase([-555, 203, 12314, 15123, 1512313, 5614, 125123, 1231, 51512], False)
f = TestCase([-555, 203, 12314, 15123, 1512313, 5614, 125123, 1231, -555], True)
g = TestCase([1, -1], False)

# Add the test cases to an array
cases = [a, b, c, d, e, f, g]

# Grab the test results by sending the cases to the function
test_results = test_cases(solution, cases)

# Print if the tests passed or failed, ideally we'd know which tests failed... but I add a new case
# and I test it. So if it fails, I know which one failed. If it passes, I can continue. Of course,
# not ideal
print("ALL TESTS PASSED" if test_results else "TEST FAILED")


