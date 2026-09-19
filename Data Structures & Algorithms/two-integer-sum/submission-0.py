class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0, len(nums)):
            lookup = target - nums[i]
            if lookup in seen:
                return [seen[lookup], i]
            else:
                seen[nums[i]] = i
        return None        