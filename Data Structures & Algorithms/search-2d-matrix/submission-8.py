class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=0
        R=len(matrix)-1

        while (L<=R):
            M = (L+R)//2
            if target<matrix[M][0]:
                R=M-1
            elif target>matrix[M][-1]:
                L=M+1
            else:
                break
        M=(L+R)//2
        l=0
        r=len(matrix[M])-1
        while l<=r:
            m=(l+r)//2
            if matrix[M][m]>target:
                r=m-1
            elif matrix[M][m]<target:
                l=m+1
            else:
                return True
        return False
             
             
        