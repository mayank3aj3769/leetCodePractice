from ast import List
  # iterative start outward edges and move inwards

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.  rotate image 90 degree
        """
        top,bottom=0,len(matrix)-1
        left,right=0,len(matrix)-1 
        
        while left<right:
            for i in range(right-left):
                top=left
                bottom=right
                temp=matrix[top][left+i]
                matrix[top][left+i]=matrix[bottom-i][left]
                matrix[bottom-i][left]=matrix[bottom][right-i]
                matrix[bottom][right-i]=matrix[top+i][right]
                matrix[top+i][right]=temp
                
            left+=1
            right-=1
        
        return

sol=Solution()
mat=[[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(mat)
