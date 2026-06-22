class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #make a hash map seen to save the numbers seen in there
        seen = set()
        #for numbers in num
        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        return False 
           