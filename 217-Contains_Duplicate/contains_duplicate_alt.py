class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numset = set()
        numset.update(nums)
        return (len(numset) != len(nums))
