"""
An array of integers called nums
An integer called target

We need to find two distinct indices in nums such that:
nums[i] + nums[j] == target

And return those indices as a list [i, j].

Key Conditions:
   Each input has exactly one solution.
   we can’t use the same element twice (i.e., i != j).
   Return the indices, not the actual numbers.

Goal (What Needs to Be Solved)
Find and return two indices of elements in nums whose sum equals the given target


How to Analyze This Problem
🔸 Input:
   nums: list of integers (length between 2 and 10⁴)
   target: integer value

🔸 Output:
   List of two integers (indices) whose values sum to target

🔸 Constraints:
   Only one valid solution exists.
   Must return indices in any order (e.g., [0,1] or [1,0] are both fine).
   Try to do better than O(n²) in time complexity.

Naive Solution (Brute-force)
Approach:
    Use two nested loops to check every pair.

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]

Time Complexity: O(n²)
   Bad for large inputs.

Optimized Solution (Using HashMap)
Idea:
    While looping through nums, keep track of numbers we've already seen using a dictionary (hashmap).
    For each number num, check if target - num is already in the map.
    If it is, return the index of that number and the current index.


def twoSum(nums, target):
    num_map = {}  # number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i


Example:

nums = [2, 7, 11, 15], target = 9
Iteration:
- i=0, num=2, complement=7 → not in map
- i=1, num=7, complement=2 → found in map! return [0,1]


Why This Works
   we store previously seen values so we can check if the pair of the current number already appeared.
   It's efficient — we only loop once over the array.

Time Complexity: O(n)
   One pass through the array.

Space Complexity: O(n)
   Because we store elements in a hash map.

More Examples
Example 1:

Input: nums = [3, 2, 4], target = 6
Check:
- 6 - 3 = 3 → not found
- 6 - 2 = 4 → not found
- 6 - 4 = 2 → found! return [1, 2]

Example 2:
nums = [3,3], target = 6
6 - 3 = 3 → already in map after first index → return [0, 1]

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        