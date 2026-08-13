class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left pointer at start (0) and right pointer at end (len(nums) - 1)

# While left pointer <= right pointer:
    # Calculate mid index
    # If element at mid equals target:
        # Return mid index
    # If element at mid is greater than target:
        # Move right pointer to mid - 1 (search left half)
    # If element at mid is less than target:
        # Move left pointer to mid + 1 (search right half)

# If loop finishes without finding target, return -1

        left = 0
        right = (len(nums)-1)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        return -1