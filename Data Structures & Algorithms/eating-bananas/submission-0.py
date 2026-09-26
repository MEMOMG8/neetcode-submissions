class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize lower bound: minimum valid eating speed is 1 banana per hour
        # Initialize upper bound: eating at rate max(piles) guarantees finishing each pile in <= 1 hour
        # Track the smallest valid speed found so far (start with upper bound as safe default)
        # Loop while the search space between low and high remains valid:
            # Calculate the candidate speed (midpoint) to evaluate
            # Calculate total hours required across all piles at this candidate speed:
                # Sum ceiling(pile / speed) for every pile
            # Feasibility check: Can all bananas be eaten within 'h' hours?
                # IF YES:
                    # Update best valid speed recorded so far to current speed
                    # Search for an even smaller valid speed in the lower/left search range    
                # IF NO:
                    # Candidate speed is too slow; search higher/right search range
        # Return the minimum valid eating speed recorded

        low = 1
        high = max(piles)
        res = high

        while low <= high:
            mid = (low + high)//2
            total_hours = sum(math.ceil(p/mid) for p in piles)

            if total_hours <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res