class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if matrix[row][0] <= target <= matrix[row][-1]:
                break

            elif matrix[row][-1] < target:
                top = row + 1

            else:
                bottom = row - 1

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            value = matrix[row][mid]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
