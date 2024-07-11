# Analyzing and Optimizing Algorithm Efficiency

## Project Overview
- This project dives into the analysis and optimization of two fundamental algorithms: Linear Search and Bubble Sort. It analyzes the time complexity of Linear Search and Bubble Sort algorithms, expressing it in Big O notation. It then implements these algorithms, tests them, and proposes optimizations to improve their efficiency.

## Algorithm 1: Linear Search
```def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### Time Complexity:
- O(n)

### Space Complexity: 
- O(1)

### Optimization:
- No significant optimization for unsorted arrays. For sorted arrays, binary search (O(log n)) is preferred.

### Optimization (Binary Search):
```
def binary_search(arr, target):
    """
        Performs binary search to find the index of the target in a sorted array.

        Args:
            arr: The sorted array to search in.
            target: The value to search for.

        Returns:
            The index of the target, or -1 if not found.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
### Time Complexity: 
- O(log n)

### Space Complexity: 
- O(1)

### Key Improvement with Binary Search:
- Binary search is significantly faster than linear search on sorted arrays, especially for large datasets. The logarithmic time complexity (O(log n)) means the number of operations grows much slower than the input size.

## Algorithm 2: Bubble Sort
```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    return arr
```
### Time Complexity:
- O(n^2)

### Space Complexity: 
- O(1)

### Optimization
```
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False: 
            break 
    return arr
```
### Optimization Explanation:
- Adds a flag (swapped) to detect early sorting. If a pass through the inner loop doesn't result in any swaps, it signifies that the array is already sorted, allowing the algorithm to terminate prematurely. 

### Time Complexity:
- O(n)

### Space Complexity: 
- O(1)

### Trade-offs:
- Readability: The optimized version is slightly less readable due to the added flag.

### Usage
- Make sure you have Python installed.
- Copy the provided code into a Python file (e.g., algorithms.py).
- Run the file from your terminal: python algorithms.py

**Accreditation Notes:**
- I used Google Gemini Advanced to help me debug some of the traceback calls that I could not solve using online resources in addition to the course materials such as Stack Overflow, and to help me with the details for this readme file and the documentation. It also helped me with the math.
- I use Stack Overflow & W3 Schools as a resource in most of my coding, mostly to help understand what is happening in the terminal errors when I cannot find the information in the course materials.
