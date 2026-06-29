class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        counter = set(nums)
        streak = 0

        for num in counter:
            if num - 1 not in counter:
                if True:
                    current_num = num
                    current_streak = 1
                    while current_num + 1 in counter:
                        current_num = current_num + 1
                        current_streak = current_streak + 1
                    streak = max(streak, current_streak)
        return streak
