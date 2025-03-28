# 官方关于状态转移方程的解释不够清楚。我来解释一下.。

# 先举个例子，nums = [1, 2, 3]，target = 35.

# 假设用1，2，3拼凑出35的总组合个数为y。我们可以考虑三种情况：

# （1）有效组合的末尾数字为1，这类组合的个数为 x1。我们把所有该类组合的末尾1去掉，那么不难发现，我们找到了一个子问题，x1即为在[1，2，3]中凑出35 - 1 = 34的总组合个数。因为我如果得到了和为34的所有组合，我只要在所有组合的最后面，拼接一个1，就得到了和为35且最后一个数字为1的组合个数了。

# （2）有效组合的末尾数字为2，这类组合的个数为 x2。我们把所有该类组合的末尾2去掉，那么不难发现，我们找到了一个子问题，x2即为在[1，2，3]中凑出35 - 2 = 33的总组合个数。因为我如果得到了和为33的所有组合，我只要在所有组合的最后面，拼接一个2，就得到了和为35且最后一个数字为2的组合个数了。

# （3）有效组合的末尾数字为3，这类组合的个数为 x3。我们把所有该类组合的末尾3去掉，那么不难发现，我们找到了一个子问题，x3即为在[1，2，3]中凑出35 - 3 = 32的总组合个数。因为我如果得到了和为32的所有组合，我只要在所有组合的最后面，拼接一个3，就得到了和为35且最后一个数字为3的组合个数了。

# 这样就简单了，y = x1 + x2 + x3。而x1，x2，x3又可以用同样的办法从子问题得到。状态转移方程get！

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        return "hello world"