This is your **Big O Cheat Sheet**. Use this as a quick reference whenever you are looking at a block of code and need to judge its efficiency.

---

## 🚀 Time Complexity: "The Speed Limit"

Time complexity tells you how many **steps** the computer takes as your data ($n$) grows.

| Big O | Name | How to Spot It (The "Vibe") | Performance |
| :--- | :--- | :--- | :--- |
| **$O(1)$** | **Constant** | No loops. Just direct math or accessing a specific index (`arr[5]`). | **Instant** |
| **$O(\log n)$** | **Logarithmic** | Data is **sorted** and you **cut the work in half** every step (Binary Search). | **Excellent** |
| **$O(n)$** | **Linear** | A **single loop** that touches every item once. | **Good** |
| **$O(n \log n)$**| **Linearithmic** | Usually seen in efficient **sorting** algorithms (like Python's `list.sort()`). | **Decent** |
| **$O(n^2)$** | **Quadratic** | **Nested loops** (a loop inside a loop). Comparing everything to everything. | **Slow** |



---

## 📦 Space Complexity: "The Memory Bucket"

Space complexity tells you how much **extra memory** you need to finish the task.

* **$O(1)$ — Constant Space:** You don't create any new lists. You might just create one or two small variables (like `total = 0`).
* **$O(n)$ — Linear Space:** You create a **new list** or a copy that grows the same size as your input. If the input has $n$ items, your new list has $n$ items.
* **$O(n^2)$ — Quadratic Space:** You create a **2D grid** (matrix) where the rows and columns are both the size of your input.

---

## 🔍 The "Newbie Eye" Identification Guide

Use these "Cheat Rules" to scan your code:

### 1. Count the Loops
* **No Loop?** $\rightarrow$ **$O(1)$**
* **1 Loop?** $\rightarrow$ **$O(n)$**
* **Loop inside a Loop?** $\rightarrow$ **$O(n^2)$**

### 2. Watch for "Hidden" Python Loops
Some Python words are actually $O(n)$ loops in disguise:
* `if x in my_list:` (Python is looping to find `x`)
* `max(my_list)` / `min(my_list)` (Python is looping to find the biggest/smallest)
* `my_string.lower()` (Python is looping through every character to change it)

### 3. The "Drop the Junk" Rule
Big O only cares about the biggest factor.
* If you have a loop ($O(n)$) followed by a nested loop ($O(n^2)$), the whole thing is just **$O(n^2)$**.
* If you have 5 separate loops, it's not $O(5n)$, it's just **$O(n)$**.

> **Pro-Tip:** If you see a problem where you need to look for something, ask yourself: *"Can I use a **Dictionary** or a **Set**?"* If you can, you often turn an $O(n)$ search into an $O(1)$ search!

---

### Comparison Visualized

| If $n = 1,000$ | Number of Operations |
| :--- | :--- |
| **$O(1)$** | 1 (Instant) |
| **$O(\log n)$** | ~10 |
| **$O(n)$** | 1,000 |
| **$O(n \log n)$** | ~10,000 |
| **$O(n^2)$** | **1,000,000** (Ouch!) |



Now that you have the cheat sheet, would you like to try refactoring a slow $O(n^2)$ piece of code into a faster $O(n)$ version together?