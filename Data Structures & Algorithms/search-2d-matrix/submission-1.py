class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #given 2D integer array amtrix and integer matrix
            #each row in matrix is in ascending order
            #first int in every row is greater that the one in previous row
        #return true if target exist
        #return false otherwise

        #get matrix dimension
        #change the 2d to a large 1d
        #set left and right pointer

        #while loop left <= right
            #calculate mid value
            #map back 1d to 2d 
                #row back to mid // n 
                #column back to mid % n

                #if matrix[row][col] == target:
                    #return True
                #if matrix[row][col] < target:
                    #left = mid + 1
                #if matrix[row][col] > target:
                    #right = mid - 1
        #return False

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m*n) - 1

        while left <= right:
            mid = (left + right)// 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            if matrix[row][col] > target:
                right = mid - 1
        return False
