# Contains Duplicate

## Problem

Given a list of numbers, determine whether the list contains any duplicate values.

The goal is to return `True` if a value appears more than once and `False` if every value is unique.

## Brute Force Approach

The brute-force approach is the simplest straightforward way to solve a problem without focusing on optimization first.

For this problem, we compare each number with the numbers that come after it. If two numbers are equal, a duplicate exists.

If all possible pairs are checked without finding a duplicate, we return `False`.

## Bottleneck

The bottleneck is the part of a solution that performs the most expensive or unnecessary work and limits the solution's performance.

In the brute-force solution, the bottleneck is the repeated comparison between pairs of numbers.

As the input becomes larger, the number of comparisons grows quickly.

## Optimized Approach

The optimized approach improves the bottleneck so the problem can be solved more efficiently.

Instead of repeatedly comparing numbers, we use a `set` to keep track of the values we have already seen.

For each number:

1. Check whether it is already in the set.
2. If it is, return `True` because a duplicate exists.
3. Otherwise, add it to the set.
4. If the entire list is processed without finding a duplicate, return `False`.

## Complexity

### Brute Force

**Time: O(n²)**

The solution uses nested loops. For each element, we compare it with the elements that come after it.

Although the inner loop becomes smaller on each iteration, the total number of comparisons still grows quadratically as the input size `n` increases.

**Space: O(1)**

The solution does not create an additional data structure that grows with the input. It only uses a constant amount of extra memory.

### Optimized

**Time: O(n) average**

We process each number once. Checking whether a value exists in a set takes **O(1) average time**, so processing `n` numbers results in O(n) average time.

**Space: O(n)**

In the worst case, when there are no duplicates, the set stores all `n` values.

## Key Lesson

The important part of optimization is not simply replacing one data structure with another.

The process is:

**Problem Brute Force Identify Bottleneck Improve Bottleneck  Analyze Complexity**

For this problem, we replaced repeated comparisons with set membership checks, reducing the average time complexity from **O(n²)** to **O(n)** at the cost of additional space.
