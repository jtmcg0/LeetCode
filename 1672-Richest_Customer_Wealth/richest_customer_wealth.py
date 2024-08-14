class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        highest = 0
        for i in accounts:
            running = 0
            for j in i:
                running += j

            if (running > highest):
                highest = running
        
        return highest
    