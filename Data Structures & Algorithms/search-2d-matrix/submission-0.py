class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        list_ = []
        for mx in matrix:
            list_.extend(mx)
        
        l, r = 0, len(list_)-1
        
        while l<=r:
            m = l + (r -l)//2
            if list_[m] < target:
                l = m + 1
            elif list_[m] > target:
                r = m - 1
            else:
                return True
        
        return False
