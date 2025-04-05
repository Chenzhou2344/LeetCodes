class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = dict()

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            if str(counts) not in mp:
                mp[str(counts)] = []
            mp[str(counts)].append(st)
        return list(mp.values())

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(s.groupAnagrams([""]))  # Output: [[""]]
    print(s.groupAnagrams(["a"]))  # Output: [["a"]]
    print(s.groupAnagrams(["abc", "cba", "bca", "bac"]))  # Output: [["abc", "cba", "bca", "bac"]]