class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set()
        indexes = {}

        for i in range(0, len(numbers)):
            lookup = target - numbers[i]
            if lookup in seen:
                return [indexes[lookup]+1, i+1]
            else:
                seen.add(numbers[i])
                indexes[numbers[i]] = i
        return None
