
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_sort = sorted(s)
#         t_sort = sorted(t)
#         if len(s_sort) != len(t_sort):
#             return False
#         for i in range(len(s_sort)):
#             if s_sort[i] != t_sort[i]:
#                 return False
#         return True
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

print(Solution().isAnagram(s = "racecar", t = "carrace"))