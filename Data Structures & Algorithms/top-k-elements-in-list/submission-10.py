from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = defaultdict(int)
        for n in nums:
            bucket[n]+=1

        buck = [[] for _ in range(len(nums)+1)]

        for num, freq in bucket.items():
            buck[freq].append(num)
        
        result = []
        for n in range(len(buck)-1,0,-1):
            for num in buck[n]:
                result.append(num)
                if len(result)==k:
                    return result