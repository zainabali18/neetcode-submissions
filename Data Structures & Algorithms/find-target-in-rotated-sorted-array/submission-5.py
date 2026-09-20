class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            #left sorted portion
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else: #target < nums[left] or taget > nums[mid]
                    left = mid+1
            # right sorted portion
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else: #target < nums[mid] or target > nums[right]
                    right = mid-1
        return -1