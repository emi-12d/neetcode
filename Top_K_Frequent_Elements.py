from collections import defaultdict
from typing import List
import heapq

# 自分の回答
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         ans_count = defaultdict(int)
#         ans = []
#         for i in nums:
#             ans_count[i] += 1
#         ans_sort = sorted(ans_count.items(), key=lambda x: x[1], reverse=True)
#         for i in range(k):
#             ans.append(ans_sort[i][0])
#         return ans

# バケットソート
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
# ヒープ
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0) # countからnum番目を取り出しなければ0を返す
        
        heap = []
        for num in count.keys():
            # 優先度付きキューに要素を挿入
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                # 優先度付きキューから最小値を取り出す
                heapq.heappop(heap)
        print(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        

print(Solution().topKFrequent(nums = [1,2,2,3,3,3,4], k = 2))