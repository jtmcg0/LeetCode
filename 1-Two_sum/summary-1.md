# 1. Two Sum

### Instructions, Examples & Constraints

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

#### Example 1:

Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].  

#### Example 2:

Input: nums = [3,2,4], target = 6  
Output: [1,2]  

#### Example 3:

Input: nums = [3,3], target = 6  
Output: [0,1]  

### Constraints:

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.

## My Solution:

- Nested loops iterate over list to find target sum
- First number is held and compared to rest of list to find corresponding sums
- If no match found, process is repeated with second number, third etc.
- If sum matching target is found, return the values of indices i and j

### Time Complexity:

$O(n^2)$ where $n$ is the number of items in the list

### Space Complexity:

$O(1)$
