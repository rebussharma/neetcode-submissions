class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top_row, btm_row = 0, ROWS - 1

        while top_row <= btm_row:
            mid_row = (top_row + btm_row) // 2
            if target < matrix[mid_row][0]:
                btm_row = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            else:
                break
        
        if not (top_row <= btm_row):
            return False
        cur_row = (top_row + btm_row) // 2
        l, r = 0, COLS - 1

        while l <= r:
            mid = l + (r - l) // 2
            if matrix[cur_row][mid] == target:
                return True
            elif matrix[cur_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
