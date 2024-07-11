# Analyzing and Optimizing Algorithm Efficiency

 

## Objective:

- In this assignment, you will apply the concepts of time complexity, Big O notation, and algorithm optimization to analyze and improve the efficiency of given algorithms. You will demonstrate your understanding of algorithm analysis, express the complexity using Big O notation, and propose optimizations to enhance performance.

 

## Problem Statement:

- You are given a set of algorithms that need to be analyzed for their time complexity and optimized for better efficiency. Your task is to determine the Big O notation for each algorithm, identify inefficiencies, and propose optimized solutions.

 

## Requirements:

### Algorithm 1: Linear Search
   - Description: Given an unsorted array of integers and a target value, find the index of the first occurrence of the target value in the array. If the target value is not found, return -1.

   - Analyze the time complexity of the linear search algorithm and express it using Big O notation.

   - Implement the linear search algorithm and test it with sample inputs.

   - Propose an optimization to improve the efficiency of the linear search algorithm, if possible.

```def linear_search(arr, target):```
#### code here

#### Sample Test Cases
```
array = [10, 23, 45, 70, 11, 15]
target = 70
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 3

target = 11
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 4

target = 99
print(f"Index of {target}: {linear_search(array, target)}")  # Output: -1
```
 

### Algorithm 2: Bubble Sort
   - Description: Given an unsorted array of integers, sort the array in ascending order using the bubble sort algorithm.

   - Analyze the time complexity of the bubble sort algorithm and express it using Big O notation.

   - Implement the bubble sort algorithm and test it with sample inputs.

   - Identify the inefficiencies in the bubble sort algorithm and propose an optimized version of the algorithm.

#### Documentation and Analysis:
   - Write a detailed document explaining your analysis, proposed optimizations, and the reasoning behind your choices.

   - Include the time complexity analysis for each algorithm, expressed using Big O notation.

   - Provide a comparison of the original and optimized versions of the algorithms, highlighting the efficiency improvements.

   - Discuss the trade-offs, if any, in terms of time complexity, space complexity, and code readability.

```def bubble_sort(arr):```

#### code here

#### Sample Test Cases
```
array = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted array: {bubble_sort(array)}")  # Output: [11, 12, 22, 25, 34, 64, 90]

array = [5, 1, 4, 2, 8]
print(f"Sorted array: {bubble_sort(array)}")  # Output: [1, 2, 4, 5, 8]
```

## Deliverables:

- Source code for the original and optimized versions of each algorithm
Documentation in README (Markdown format) with the analysis, optimizations, and explanations
Screenshot of the code from VS Code
 

## Submission Guidelines:

- Create a new personal repository for your assignment.

- Organize your source code and documentation files within the assignment directory.

- Include: Documentation file (Markdown format) with the analysis, optimizations, and explanations -- as the README

- ON CANVAS Submit the GitHub repository URL and a screenshot of your solution code in VS Code.