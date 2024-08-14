class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexI = 0
        for i in nums:
            indexJ = 0
            for j in nums:
                if (i + j == target) and (indexI != indexJ):
                    result = [indexI, indexJ]
                    return result
                indexJ += 1
            indexI += 1