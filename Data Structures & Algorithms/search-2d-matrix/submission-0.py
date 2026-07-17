class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #input: A matrix 2D array of array and a target
        #output: If the target exist in the matrix

        #intutation binary search: 
        # 1. find the array where the target may exist
        # 2. Check if target exist in that array

        l = 0
        r = len(matrix) - 1
        target_row = None
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = matrix[mid]
                break
            elif matrix[mid][0] >= target:
                r = mid - 1
            else:
                l = mid + 1
        
        if target_row:
            l, r = 0, len(target_row) - 1
            while l <= r:
                mid = l + ((r - l) // 2)
                if target_row[mid] == target:
                    return True
                elif target_row[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
