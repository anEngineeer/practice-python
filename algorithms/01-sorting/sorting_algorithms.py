"""
Sorting Algorithms Implementation

A comprehensive collection of sorting algorithms with analysis and comparisons.
"""

import time
import random
from typing import List, Callable


class SortingAlgorithms:
    """Collection of sorting algorithms with performance analysis"""
    
    @staticmethod
    def bubble_sort(arr: List[int]) -> List[int]:
        """
        Bubble Sort - Repeatedly steps through the list, compares adjacent elements
        and swaps them if they are in the wrong order.
        
        Time: O(n²) average and worst case, O(n) best case
        Space: O(1)
        Stable: Yes
        """
        arr = arr.copy()  # Don't modify original
        n = len(arr)
        
        for i in range(n):
            swapped = False
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            # If no swapping occurred, array is sorted
            if not swapped:
                break
        
        return arr
    
    @staticmethod
    def selection_sort(arr: List[int]) -> List[int]:
        """
        Selection Sort - Finds the minimum element and places it at the beginning
        
        Time: O(n²) all cases
        Space: O(1)
        Stable: No
        """
        arr = arr.copy()
        n = len(arr)
        
        for i in range(n):
            # Find minimum element in remaining unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # Swap the found minimum element with first element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr
    
    @staticmethod
    def insertion_sort(arr: List[int]) -> List[int]:
        """
        Insertion Sort - Builds the sorted array one item at a time
        
        Time: O(n²) average and worst case, O(n) best case
        Space: O(1) 
        Stable: Yes
        """
        arr = arr.copy()
        
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            # Move elements greater than key one position ahead
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
        
        return arr
    
    @staticmethod
    def merge_sort(arr: List[int]) -> List[int]:
        """
        Merge Sort - Divide and conquer algorithm
        
        Time: O(n log n) all cases
        Space: O(n)
        Stable: Yes
        """
        if len(arr) <= 1:
            return arr.copy()
        
        def merge(left: List[int], right: List[int]) -> List[int]:
            """Merge two sorted arrays"""
            result = []
            i = j = 0
            
            # Merge elements in sorted order
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            # Add remaining elements
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        # Divide array into halves
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        
        return merge(left, right)
    
    @staticmethod
    def quick_sort(arr: List[int]) -> List[int]:
        """
        Quick Sort - Divide and conquer with pivot partitioning
        
        Time: O(n log n) average case, O(n²) worst case
        Space: O(log n) average case
        Stable: No
        """
        if len(arr) <= 1:
            return arr.copy()
        
        def partition(arr: List[int], low: int, high: int) -> int:
            """Partition array around pivot"""
            pivot = arr[high]  # Choose last element as pivot
            i = low - 1  # Index of smaller element
            
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        def quick_sort_helper(arr: List[int], low: int, high: int):
            """Recursive helper function"""
            if low < high:
                pi = partition(arr, low, high)
                quick_sort_helper(arr, low, pi - 1)
                quick_sort_helper(arr, pi + 1, high)
        
        result = arr.copy()
        quick_sort_helper(result, 0, len(result) - 1)
        return result
    
    @staticmethod
    def heap_sort(arr: List[int]) -> List[int]:
        """
        Heap Sort - Uses binary heap data structure
        
        Time: O(n log n) all cases
        Space: O(1)
        Stable: No
        """
        arr = arr.copy()
        n = len(arr)
        
        def heapify(arr: List[int], n: int, i: int):
            """Maintain heap property"""
            largest = i  # Initialize largest as root
            left = 2 * i + 1
            right = 2 * i + 2
            
            # Check if left child is larger than root
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            # Check if right child is larger than largest so far
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            # Change root if needed
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        
        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # Swap
            heapify(arr, i, 0)
        
        return arr


def benchmark_sorting_algorithms():
    """Benchmark all sorting algorithms with different array sizes"""
    print("=== Sorting Algorithms Benchmark ===")
    
    algorithms = {
        'Bubble Sort': SortingAlgorithms.bubble_sort,
        'Selection Sort': SortingAlgorithms.selection_sort,
        'Insertion Sort': SortingAlgorithms.insertion_sort,
        'Merge Sort': SortingAlgorithms.merge_sort,
        'Quick Sort': SortingAlgorithms.quick_sort,
        'Heap Sort': SortingAlgorithms.heap_sort,
    }
    
    test_sizes = [100, 500, 1000]
    
    for size in test_sizes:
        print(f"\n--- Array Size: {size} ---")
        
        # Generate random array
        test_array = [random.randint(1, 1000) for _ in range(size)]
        
        for name, algorithm in algorithms.items():
            start_time = time.time()
            sorted_array = algorithm(test_array)
            end_time = time.time()
            
            # Verify correctness
            is_sorted = sorted_array == sorted(test_array)
            
            print(f"{name:15} | {end_time - start_time:.4f}s | {'✓' if is_sorted else '✗'}")


def demonstrate_sorting():
    """Demonstrate sorting algorithms with a small example"""
    print("=== Sorting Demonstration ===")
    
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    print()
    
    algorithms = {
        'Bubble Sort': SortingAlgorithms.bubble_sort,
        'Selection Sort': SortingAlgorithms.selection_sort, 
        'Insertion Sort': SortingAlgorithms.insertion_sort,
        'Merge Sort': SortingAlgorithms.merge_sort,
        'Quick Sort': SortingAlgorithms.quick_sort,
        'Heap Sort': SortingAlgorithms.heap_sort,
    }
    
    for name, algorithm in algorithms.items():
        sorted_array = algorithm(test_array)
        print(f"{name:15}: {sorted_array}")


def analyze_complexity():
    """Display time and space complexity analysis"""
    print("\n=== Complexity Analysis ===")
    
    complexity_table = [
        ("Algorithm", "Best Case", "Average Case", "Worst Case", "Space", "Stable"),
        ("Bubble Sort", "O(n)", "O(n²)", "O(n²)", "O(1)", "Yes"),
        ("Selection Sort", "O(n²)", "O(n²)", "O(n²)", "O(1)", "No"),
        ("Insertion Sort", "O(n)", "O(n²)", "O(n²)", "O(1)", "Yes"),
        ("Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "Yes"),
        ("Quick Sort", "O(n log n)", "O(n log n)", "O(n²)", "O(log n)", "No"),
        ("Heap Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(1)", "No"),
    ]
    
    # Print table with formatting
    for row in complexity_table:
        print(f"{row[0]:15} | {row[1]:10} | {row[2]:12} | {row[3]:10} | {row[4]:8} | {row[5]:6}")
        if row[0] == "Algorithm":
            print("-" * 80)


if __name__ == "__main__":
    demonstrate_sorting()
    analyze_complexity()
    
    # Uncomment to run benchmarks (takes some time)
    # benchmark_sorting_algorithms()
    
    print("\n=== Key Takeaways ===")
    print("1. Merge Sort: Consistent O(n log n), stable, but uses O(n) space")
    print("2. Quick Sort: Average O(n log n), in-place, but O(n²) worst case")  
    print("3. Heap Sort: Guaranteed O(n log n), in-place, but not stable")
    print("4. Insertion Sort: Best for small arrays or nearly sorted data")
    print("5. Bubble/Selection: Educational value, but inefficient for large data")