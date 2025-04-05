# class Solution:
#     def findAnagrams(self, s: str, p: str) -> list[int]:
#         s_len, p_len = len(s), len(p)
        
#         if s_len < p_len:
#             return []

#         ans = []
#         s_count = [0] * 26
#         p_count = [0] * 26
#         for i in range(p_len):
#             s_count[ord(s[i]) - 97] += 1
#             p_count[ord(p[i]) - 97] += 1

#         if s_count == p_count:
#             ans.append(0)

#         for i in range(s_len - p_len):
#             s_count[ord(s[i]) - 97] -= 1
#             s_count[ord(s[i + p_len]) - 97] += 1
            
#             if s_count == p_count:
#                 ans.append(i + 1)

#         return ans

# 自己掌握滑窗后的解答
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_count = [0] * 26
        p_count = [0] * 26



        plen = len(p)
        slen = len(s)
        results = []
        if slen < plen:
            return []
        for i in range(plen):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
    

        for k in range(slen-plen+1):
            if s_count == p_count:
                results.append(k)
            if k==slen-plen:
                break
            s_count[ord(s[k])-97]-=1
            s_count[ord(s[k + plen]) - 97] += 1
       
        return  results

if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]
    print(s.findAnagrams("abab", "ab"))          # Output: [0, 1, 2]
