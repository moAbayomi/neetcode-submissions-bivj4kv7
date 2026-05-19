class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] == target:
                return True
            if row[-1] > target:
                for i in row:
                    if i == target:
                        return True
        return False
        