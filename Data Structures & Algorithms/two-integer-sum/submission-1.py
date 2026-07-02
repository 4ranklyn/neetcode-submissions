class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        note={}
        for x in range(len(nums)):
            a = target - nums[x]
            if a in note:
                return [note[a],x]
            else:
                note[nums[x]] = x