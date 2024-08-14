class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        lastnum = -110

        for item in nums:
            if item == lastnum:
                return True
            else:
                lastnum = item
        return False
    