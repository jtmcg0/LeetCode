# 217. Contains Duplicate

### Instructions, Examples & Constraints
 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#### Example 1:

Input: nums = [1,2,3,1]  
Output: true  

#### Example 2:

Input: nums = [1,2,3,4]  
Output: false  

#### Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]  
Output: true

### Constraints:

- 1 <= nums.length <= 105  
- -109 <= nums[i] <= 109

## My Solution:

- Sort list of integers into numerical order
- Duplicates will be grouped together
- Iterate through list checking if current number is equal to last
- Return true if duplicate found

### Time Complexity:

$O(n \log n)$ where $n$ is the number of items in the list

### Space Complexity:

$O(1)$

## Alternate Solution

- Assign number list to a set
- Set is list with any duplicates removed
- If length of set and length of list differ, list has duplicates
- Compare length of set to length of list to get boolean result and return it

### Alternate Time Complexity

$O(n)$ where $n$ is the number of items in the list

### Alternate Space Complexity

$O(n)$ where $n$ is the number of items in the list