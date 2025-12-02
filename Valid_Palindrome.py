import re


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # 非英数字文字用の正規表現パターンを定義
#         pattern = r"[^a-zA-Z0-9\s]"
#         # re.sub() を使用して特殊文字を空文字に置換
#         s = re.sub(pattern, "", s)
#         s = s.replace(" ", "")
#         s_clean = s.lower()
#         for i in range(len(s_clean)):
#             if s_clean[i] != s_clean[len(s_clean)-1-i]:
#                 return False
#         return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum(): # 英数字かどうか判定する
                newStr += c.lower()
        return newStr == newStr[::-1]
  

print(Solution().isPalindrome(s = "tab a cat"))