class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) time and space complexity
        seen = set()

        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)