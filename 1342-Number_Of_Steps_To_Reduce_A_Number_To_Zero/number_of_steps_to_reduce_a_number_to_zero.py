class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step = 0
        while num > 0:
            if num % 2 != 0:
                num -= 1
                step += 1
            else:
                num = num/2
                step += 1
        return step
    