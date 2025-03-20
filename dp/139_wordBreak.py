class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(1,len(s)+1):
            ss = s[:i]
            for j in range(len(wordDict)):
                if i - len(wordDict[j])>=0 and ss[i-len(wordDict[j]):]==wordDict[j] and dp[i-len(wordDict[j])]:
                    dp[i] = True
                    break
        return dp[-1]

if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet","code"]
    print(Solution().wordBreak(s, wordDict)) # True

    s = "applepenapple"
    wordDict = ["apple","pen"]
    print(Solution().wordBreak(s, wordDict)) # True

    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(Solution().wordBreak(s, wordDict)) # False