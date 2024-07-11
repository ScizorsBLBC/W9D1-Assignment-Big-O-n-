# Algorithm 1: Linear Search
def linear_search(arr, target):
    """
        Performs linear search to find the index of the target in the array.

        Args:
            arr: The unsorted array to search in.
            target: The value to search for.

        Returns:
            The index of the first occurrence of the target, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

array = [10, 23, 45, 70, 11, 15]
target = 70
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 3

target = 11
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 4

target = 99
print(f"Index of {target}: {linear_search(array, target)}")  # Output: -1


'''
Sample Test Cases:

Time Complexity: O(n) 

Space Complexity: O(1)

- The algorithm uses a constant amount of extra space regardless of the input size. It only needs variables to keep track of the loop index (i) and potentially the found index, all of which take constant space.

Optimization (Linear Search):

- Linear search on an unsorted array has no significant optimization in terms of time complexity. However, if the array were sorted, we could use binary search (O(log n)).
'''

# Optimization (Binary Search):
def binary_search(arr, target, original_array):
    """
        Performs binary search to find the index of the target in a sorted array.

        Args:
            arr: The sorted array to search in.
            target: The value to search for.
            original_array: The unsorted array to find the original index from.

        Returns:
            The index of the target in the original array, or -1 if not found.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            # Find index in original array 
            original_index = original_array.index(arr[mid]) 
            return original_index
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Sort a copy of the array for binary search
sorted_array = sorted(array.copy())

# Test Cases (using the original and sorted arrays)
targets = [70, 11, 99]
for target in targets:
    linear_result = linear_search(array, target)
    binary_result = binary_search(sorted_array, target, array) # Pass the original array to binary_search
    print(f"Binary Search Index of {target}: {binary_result}")

'''
Time Complexity: O(log n)

Space Complexity: O(1)

- Binary search also uses a constant amount of extra space for its variables (low, high, mid).

Key Improvement with Binary Search:
- Binary search is significantly faster than linear search on sorted arrays, especially for large datasets. The logarithmic time complexity (O(log n)) means the number of operations grows much slower than the input size.
'''

# Algorithm 2: Bubble Sort
def bubble_sort(arr):
    """
        Sorts the array in ascending order using the bubble sort algorithm.

        Args:
            arr: The unsorted array to sort.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place 
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    return arr

array = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted array: {bubble_sort(array)}")  # Output: [11, 12, 22, 25, 34, 64, 90]

array = [5, 1, 4, 2, 8]
print(f"Sorted array: {bubble_sort(array)}")  # Output: [1, 2, 4, 5, 8]

'''
Sample Test Cases (as provided in the guidelines)

Time Complexity (Bubble Sort): O(n^2)

Space Complexity: O(1)

- This is an in-place sorting algorithm. It modifies the original array directly and doesn't require any additional data structures that scale with the input size. The only extra space is used for loop indices.
'''

# Optimization (Bubble Sort):
def optimized_bubble_sort(arr):
    """
        Optimized bubble sort with a flag to detect early sorting.

        Args:
            arr: The unsorted array to sort.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break 
        if swapped == False: 
            break 
    return arr

array = [64, 34, 25, 12, 22, 11, 90]
print(f"Optimized sorted array: {optimized_bubble_sort(array)}")  # Output: [11, 12, 22, 25, 34, 64, 90]

array = [5, 1, 4, 2, 8]
print(f"Optimized sorted array: {optimized_bubble_sort(array)}")  # Output: [1, 2, 4, 5, 8]

'''
Optimization Explanation:

- The optimized version adds a flag (swapped). If a pass through the inner loop doesn't perform any swaps, it means the array is already sorted, and the algorithm can stop early. 

Time Complexity (Optimized): O(n)

Space Complexity: O(1)

- The optimized version introduces a boolean variable but doesn't change the overall space complexity. It remains an in-place sorting algorithm with constant extra space.

Key Improvements:

- Early Termination: Bubble sort can now terminate early if the array gets sorted in fewer passes.

- Reduced Comparisons: The optimized version might perform fewer comparisons, especially in nearly sorted arrays.

Trade-offs:

- Readability: The optimized version is slightly less readable due to the added flag.
'''