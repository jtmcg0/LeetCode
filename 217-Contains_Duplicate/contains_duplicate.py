# 217. Contains Duplicate

'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

'''
My Solution:

Sort list of integers into numerical order
Duplicates will be grouped together
Iterate through list checking if current number is equal to last
Return true if duplicate found

Time Complexity: O(NLogN)
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        lastnum = -1

        for item in nums:
            if item == lastnum:
                return True
            else:
                lastnum = item
        return False
    