from typing import List

# 自分の回答
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = [] # 回答のリスト
#         strs_sort_list = [] # ソートした文字列の比較用リスト
#         strs_sort = ""  # ソートした文字列の保存
#         for i in strs:
#             strs_sort = sorted(i) # 文字列ソート
            
#             if strs_sort in strs_sort_list: # ソートした文字列が比較用にあるかどうか
#                 ans[strs_sort_list.index(strs_sort)].append(i)
#             else:
#                 strs_sort_list.append(strs_sort)
#                 ans.append([i])
#         return ans

# 別解
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s)) # ソートしたリスト文字列を結合
            res[sortedS].append(s) # defaultdictは初期値を設定不要
        print(res)
        return list(res.values())

        
print(Solution().groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))