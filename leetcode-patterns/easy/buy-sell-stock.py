
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        count = 0
        max_proft = 0

        while(count < len(prices)):
            if prices[count] < buy:
                buy = prices[count]
                sell = prices[count]
            elif prices[count] > sell:
                sell = prices[count]
            count += 1
            if (sell-buy) > max_proft:
                max_proft = sell-buy
        return(max_proft)




class TestCase:
    def __init__(self, num, expected_output):
        self.num = num
        self.expected_output = expected_output

def run_tests(solution, testcases):
    for case in testcases:
        if solution.maxProfit(case.num) != case.expected_output:
            return False
    return True

solution = Solution()

a = TestCase([7,1,5,3,6,4], 5)
b = TestCase([7,6,4,3,1], 0)
c = TestCase([99, 2, 56, 1, 1, 100], 99)
d = TestCase([], 0)
e = TestCase([2, 4, 1], 2)

cases = [a, b, c, e]

print("TESTS PASSED" if run_tests(solution, cases) else "TEST FAILED")

