class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #given nums in sorted ascending order
        #given a target

        #make a function to search for target within nums. 
            #If exist return index
            #if not return -1
        
        #make pointers left and right

        #while left <= right
            #mid = (left + right)//2
                #nums[mid] == target
                    #return index of mid
                #if nums[mid] < target
                    #left = mid + 1
                #if nums[mid] > target
                    #right = mid - 1
        #return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return -1





