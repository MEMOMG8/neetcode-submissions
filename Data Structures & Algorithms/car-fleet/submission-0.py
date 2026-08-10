class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        fleets = 0
        prev_time = 0

        for p, s in pairs:
            time = (target - p) / s
            if time > prev_time:
                fleets += 1
                prev_time = time
        return fleets