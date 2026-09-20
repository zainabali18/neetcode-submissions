from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if sum(ceil(pile / mid) for pile in piles) > h:
                left = mid + 1
            else:
                right = mid
        return left
