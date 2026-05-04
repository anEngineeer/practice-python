# Algorithms

Implementation and analysis of fundamental algorithms essential for problem-solving and technical interviews.

## ⚡ Topics Covered

### 01 - Sorting Algorithms
- **Elementary Sorts**: Bubble, Selection, Insertion
- **Efficient Sorts**: Merge Sort, Quick Sort, Heap Sort
- **Specialized Sorts**: Counting Sort, Radix Sort, Bucket Sort
- **Analysis**: Time/space complexity, stability, in-place sorting

### 02 - Searching Algorithms  
- **Linear Search**: Sequential search through data
- **Binary Search**: Divide and conquer on sorted data
- **Search Variations**: First/last occurrence, rotated arrays
- **String Searching**: KMP, Boyer-Moore algorithms

### 03 - Recursion
- **Recursion Fundamentals**: Base cases, recursive cases
- **Classic Problems**: Factorial, Fibonacci, Tower of Hanoi
- **Backtracking**: N-Queens, Sudoku solver, maze solving
- **Optimization**: Memoization, tail recursion

### 04 - Dynamic Programming
- **DP Principles**: Overlapping subproblems, optimal substructure
- **Classic DP**: Knapsack, Longest Common Subsequence
- **Advanced DP**: Edit distance, matrix chain multiplication
- **Optimization**: Space optimization, bottom-up vs top-down

### 05 - Graph Algorithms
- **Traversals**: Breadth-First Search (BFS), Depth-First Search (DFS)
- **Shortest Path**: Dijkstra's, Bellman-Ford, Floyd-Warshall
- **Minimum Spanning Tree**: Kruskal's, Prim's algorithms
- **Advanced**: Topological sorting, strongly connected components

### 06 - Greedy Algorithms
- **Greedy Strategy**: Making locally optimal choices
- **Classic Problems**: Activity selection, coin change
- **Graph Applications**: Huffman coding, minimum spanning tree
- **Analysis**: When greedy works vs when it doesn't

## 📊 Algorithm Complexity Chart

### Sorting Algorithms
| Algorithm | Best Case | Average Case | Worst Case | Space | Stable |
|-----------|-----------|--------------|------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

### Graph Algorithms
| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| BFS | O(V + E) | O(V) | Shortest path (unweighted) |
| DFS | O(V + E) | O(V) | Cycle detection, topological sort |
| Dijkstra | O((V + E) log V) | O(V) | Shortest path (weighted) |
| Bellman-Ford | O(VE) | O(V) | Negative edge weights |
| Kruskal | O(E log E) | O(V) | Minimum spanning tree |

## 🎯 Problem-Solving Strategy

### 1. Understand the Problem
- Read carefully and identify constraints
- Clarify input/output format
- Consider edge cases

### 2. Choose the Right Approach
- **Brute Force**: Try all possibilities (baseline)
- **Divide & Conquer**: Break into smaller subproblems
- **Dynamic Programming**: Optimal substructure + overlapping subproblems
- **Greedy**: Make locally optimal choices
- **Backtracking**: Explore all possibilities with pruning

### 3. Analyze Complexity
- Time complexity: How runtime scales with input size
- Space complexity: How memory usage scales with input size
- Trade-offs: Time vs space, readability vs performance

### 4. Implement and Test
- Start with brute force, then optimize
- Test with edge cases and large inputs
- Consider integer overflow, empty inputs, etc.

## 🏆 Interview Preparation

### Must-Know Algorithms
1. **Binary Search** - O(log n) searching
2. **Merge Sort** - O(n log n) stable sorting  
3. **DFS/BFS** - Graph traversal fundamentals
4. **Dynamic Programming** - Optimization technique
5. **Two Pointers** - Array/string manipulation

### Common Patterns
- **Sliding Window**: Subarray/substring problems
- **Two Pointers**: Pair/triplet finding
- **Fast & Slow Pointers**: Cycle detection
- **Top K Elements**: Heap-based solutions
- **Tree/Graph DFS**: Recursive exploration

## 📚 Practice Resources
- **LeetCode**: 1000+ algorithmic problems
- **HackerRank**: Structured learning paths  
- **Codeforces**: Competitive programming
- **InterviewBit**: Interview-focused problems