class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList=set()

        for num in nums:
            if num in newList:
                return True

            newList.add(num)

        return False
