# Problem:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Constraints:
# 1 <= n <= 45

from typing import List # Need this import to use 'List'

class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n+1)
        ways[0] = 1
        ways[1] = 1
        ans = 2
        for i in range(2,n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return(ways[n])



class TestCase:
    def __init__(self, num, expected_output):
        self.num = num
        self.expected_output = expected_output

def run_tests(solution, testcases):
    for case in testcases:
        if solution.climbStairs(case.num) != case.expected_output:
            return False
    return True

solution = Solution()

a = TestCase(2, 2)
b = TestCase(3, 3)
c = TestCase(5, 8)

cases = [a, b, c]

print("TESTS PASSED" if run_tests(solution, cases) else "TEST FAILED")

