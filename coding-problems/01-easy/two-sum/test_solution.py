"""
Unit tests for Two Sum problem solutions
"""

import unittest
from solution import Solution


class TestTwoSum(unittest.TestCase):
    """Test cases for all Two Sum solution approaches"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.solution = Solution()
        
        # Test all approaches
        self.approaches = [
            self.solution.two_sum_brute_force,
            self.solution.two_sum_hash_table,
            self.solution.two_sum_two_pointers,
        ]
    
    def verify_result(self, nums, target, result):
        """Helper method to verify if result is correct"""
        if len(result) != 2:
            return False
        
        i, j = result
        if i < 0 or i >= len(nums) or j < 0 or j >= len(nums):
            return False
        
        if i == j:
            return False
        
        return nums[i] + nums[j] == target
    
    def test_basic_cases(self):
        """Test basic functionality with provided examples"""
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]
        
        for approach in self.approaches:
            with self.subTest(approach=approach.__name__):
                for nums, target, expected in test_cases:
                    result = approach(nums, target)
                    self.assertTrue(
                        self.verify_result(nums, target, result),
                        f"Failed for {nums}, target={target}, got {result}"
                    )
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        test_cases = [
            ([-1, -2, -3, -4, -5], -8, [2, 4]),  # -3 + -5 = -8
            ([-3, 4, 3, 90], 0, [0, 2]),         # -3 + 3 = 0
            ([1, -1, 0], 0, [0, 1]),             # 1 + (-1) = 0
        ]
        
        for approach in self.approaches:
            with self.subTest(approach=approach.__name__):
                for nums, target, expected in test_cases:
                    result = approach(nums, target)
                    self.assertTrue(
                        self.verify_result(nums, target, result),
                        f"Failed for {nums}, target={target}, got {result}"
                    )
    
    def test_edge_cases(self):
        """Test edge cases"""
        test_cases = [
            ([0, 4, 3, 0], 0, [0, 3]),     # zeros
            ([1, 2], 3, [0, 1]),           # minimum size
            ([5, 5, 5], 10, [0, 1]),       # all same elements
        ]
        
        for approach in self.approaches:
            with self.subTest(approach=approach.__name__):
                for nums, target, expected in test_cases:
                    result = approach(nums, target)
                    self.assertTrue(
                        self.verify_result(nums, target, result),
                        f"Failed for {nums}, target={target}, got {result}"
                    )
    
    def test_large_numbers(self):
        """Test with large numbers within constraints"""
        test_cases = [
            ([1000000000, -1000000000], 0, [0, 1]),
            ([999999999, 1], 1000000000, [0, 1]),
        ]
        
        for approach in self.approaches:
            with self.subTest(approach=approach.__name__):
                for nums, target, expected in test_cases:
                    result = approach(nums, target)
                    self.assertTrue(
                        self.verify_result(nums, target, result),
                        f"Failed for {nums}, target={target}, got {result}"
                    )
    
    def test_performance_hash_table(self):
        """Test performance characteristics (mainly for hash table approach)"""
        # Create a large array where the answer is at the end
        large_nums = list(range(1000)) + [999, 1]  # Answer: [999, 1000]
        target = 1000  # 999 + 1 = 1000
        
        # Hash table should find this quickly
        result = self.solution.two_sum_hash_table(large_nums, target)
        self.assertTrue(self.verify_result(large_nums, target, result))
    
    def test_result_format(self):
        """Test that results are in the correct format"""
        nums = [2, 7, 11, 15]
        target = 9
        
        for approach in self.approaches:
            with self.subTest(approach=approach.__name__):
                result = approach(nums, target)
                
                # Should return a list
                self.assertIsInstance(result, list)
                
                # Should have exactly 2 elements
                self.assertEqual(len(result), 2)
                
                # Elements should be integers
                self.assertIsInstance(result[0], int)
                self.assertIsInstance(result[1], int)
                
                # Should be valid indices
                self.assertGreaterEqual(result[0], 0)
                self.assertGreaterEqual(result[1], 0)
                self.assertLess(result[0], len(nums))
                self.assertLess(result[1], len(nums))
                
                # Should not be the same index
                self.assertNotEqual(result[0], result[1])


class TestTwoSumPerformance(unittest.TestCase):
    """Performance tests for Two Sum solutions"""
    
    def setUp(self):
        self.solution = Solution()
    
    def test_hash_table_vs_brute_force(self):
        """Compare performance of hash table vs brute force (conceptual)"""
        # This is more of a conceptual test - in practice you'd use timing
        
        # For small arrays, both should work
        small_nums = [1, 2, 3, 4, 5]
        target = 9  # 4 + 5 = 9
        
        result1 = self.solution.two_sum_brute_force(small_nums, target)
        result2 = self.solution.two_sum_hash_table(small_nums, target)
        
        # Both should find valid solutions
        self.assertTrue(self.verify_result(small_nums, target, result1))
        self.assertTrue(self.verify_result(small_nums, target, result2))
    
    def verify_result(self, nums, target, result):
        """Helper method to verify if result is correct"""
        if len(result) != 2:
            return False
        
        i, j = result
        if i < 0 or i >= len(nums) or j < 0 or j >= len(nums):
            return False
        
        if i == j:
            return False
        
        return nums[i] + nums[j] == target


if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)
    
    # Or run specific test classes
    # unittest.main(argv=[''], testRunner=unittest.TextTestRunner(verbosity=2), exit=False)