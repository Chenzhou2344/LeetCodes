# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         max_length = 0
#         if n == 0:
#             return max_length
#         subs = ""
#         i = 0
#         while i<n:
#             print(f"subs: {subs}, i: {i}, s[i]: {s[i]}")
#             if s[i] not in subs:
#                 subs = subs+s[i]
#                 i+=1
#             else:
#                 max_length = max(max_length,len(subs))
#                 for j in range(len(subs)):
#                     if subs[j]==s[i]:
#                         subs=subs[j+1:]+s[i]
#                         break
#                 i+=1
#         max_length = max(max_length,len(subs))
        
#         return max_length

#想法和原理与官方题解相同，只不过不懂滑动窗口的具体实现
#官方题解:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
    
if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    # print(s.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    # print(s.lengthOfLongestSubstring("pwwkew"))    # Output: 3
    print(s.lengthOfLongestSubstring("aabaab!bb")) # Output: 3
    # print(s.lengthOfLongestSubstring(" "))         # Output: 1