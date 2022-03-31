# dynamic programming - iterative
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i): # ignore the first and last position for every row
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal