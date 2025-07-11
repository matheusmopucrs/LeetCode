import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  
    

class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    def test_example_two(self):
        nums = [3, 2, 4]
        target = 6
        expected_output = [1, 2]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    def test_example_three(self):
        nums = [3, 3]
        target = 6
        expected_output = [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    def test_no_solution(self):
        nums = [1, 2, 3]
        target = 7
        expected_output = []
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    def test_large_numbers(self):
        nums = [1000, 2000, 3000, 4000]
        target = 5000
        expected_output = [0, 3]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected_output = [2, 4]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)