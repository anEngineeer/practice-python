"""
Problem: Two Sum
Difficulty: Easy
Source: LeetCode #1
Tags: array, hash-table

Problem Description:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

You can return the answer in any order.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

from typing import List


class Solution:
    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force Approach: Check all pairs
        
        Time Complexity: O(n²) - nested loops
        Space Complexity: O(1) - only using constant extra space
        
        For each element, check if target - element exists in the rest of array.
        """
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []  # No solution found (shouldn't happen per constraints)
    
    def two_sum_hash_table(self, nums: List[int], target: int) -> List[int]:
        """
        Hash Table Approach: Use dictionary to store complements
        
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(n) - hash table can store up to n elements
        
        For each element x, check if (target - x) has been seen before.
        If yes, we found our pair. If no, store x with its index.
        """
        seen = {}  # value -> index mapping
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return []  # No solution found (shouldn't happen per constraints)
    
    def two_sum_two_pointers(self, nums: List[int], target: int) -> List[int]:
        """
        Two Pointers Approach: Only works if we can sort the array
        
        NOTE: This approach changes the original indices, so we need to 
        track original positions. Generally not preferred for this problem.
        
        Time Complexity: O(n log n) - due to sorting
        Space Complexity: O(n) - for storing (value, index) pairs
        """
        # Create pairs of (value, original_index)
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # Sort by value
        indexed_nums.sort()
        
        left, right = 0, len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                # Return original indices
                return sorted([indexed_nums[left][1], indexed_nums[right][1]])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []


def test_solutions():
    """Test all solution approaches with various test cases"""
    solution = Solution()
    
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ]
    
    approaches = [
        ("Brute Force", solution.two_sum_brute_force),
        ("Hash Table", solution.two_sum_hash_table),
        ("Two Pointers", solution.two_sum_two_pointers),
    ]
    
    print("=== Two Sum Solutions Test ===")
    
    for approach_name, method in approaches:
        print(f"\n--- {approach_name} ---")
        all_passed = True
        
        for i, (nums, target, expected) in enumerate(test_cases, 1):
            result = method(nums, target)
            
            # Check if result is correct (order doesn't matter)
            is_correct = (
                len(result) == 2 and 
                result[0] != result[1] and
                nums[result[0]] + nums[result[1]] == target
            )
            
            status = "✓" if is_correct else "✗"
            print(f"Test {i}: {status} nums={nums}, target={target} -> {result}")
            
            if not is_correct:
                all_passed = False
        
        print(f"All tests passed: {all_passed}")


def analyze_approaches():
    """Analyze the different approaches"""
    print("\n=== Approach Analysis ===")
    
    print("1. Brute Force:")
    print("   + Simple to understand and implement")
    print("   + No extra space needed")
    print("   - O(n²) time complexity")
    print("   - Inefficient for large arrays")
    
    print("\n2. Hash Table:")
    print("   + O(n) time complexity - optimal")
    print("   + Single pass through array")
    print("   - O(n) space complexity")
    print("   - Best approach for this problem")
    
    print("\n3. Two Pointers:")
    print("   + O(n) space complexity after sorting")
    print("   + Good for sorted array variants")
    print("   - O(n log n) time due to sorting")
    print("   - Loses original indices (needs extra work)")
    print("   - Not ideal for this specific problem")


def demonstrate_step_by_step():
    """Show step-by-step execution of the optimal solution"""
    print("\n=== Step-by-Step Demonstration ===")
    
    nums = [2, 7, 11, 15]
    target = 9
    
    print(f"Input: nums = {nums}, target = {target}")
    print("\nHash Table Approach:")
    
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        print(f"Step {i+1}: num = {num}, complement = {target} - {num} = {complement}")
        
        if complement in seen:
            result = [seen[complement], i]
            print(f"Found! complement {complement} is at index {seen[complement]}")
            print(f"Answer: [{seen[complement]}, {i}]")
            break
        else:
            seen[num] = i
            print(f"Store: seen[{num}] = {i}, seen = {seen}")
    
    print(f"\nVerification: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]} = {target} ✓")


if __name__ == "__main__":
    test_solutions()
    analyze_approaches()  
    demonstrate_step_by_step()
    
    print("\n=== Key Learning Points ===")
    print("1. Hash tables can reduce O(n²) to O(n) for lookup problems")
    print("2. Trade-off between time and space complexity")
    print("3. Always consider the constraints and requirements")
    print("4. Multiple solutions exist - choose based on context")
    print("5. Test with edge cases (duplicates, negatives, etc.)")