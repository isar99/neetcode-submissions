class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_ele = len(nums)//2
        for i in nums:
            if nums.count(i) > major_ele:
                return i
        return 0

        