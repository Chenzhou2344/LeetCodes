# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         s = list(s)
#         def rst(s,k):
#             if len(s)<k:
#                 start = 0
#                 end = len(s)-1
#             else:
#                 start = 0
#                 end = k-1

#             while(start<=end):
#                 tmp = s[start]
#                 s[start] = s[end]
#                 s[end] = tmp
#                 start+=1
#                 end-=1

#             return s
        
#         n_torev = len(s)//(2*k)
#         for i in range(n_torev):
#             s[i*2*k:(i+1)*2*k] = rst(s[i*2*k:(i+1)*2*k],k)
#         s[n_torev*2*k:] = rst(s[n_torev*2*k:],k)

#         return ''.join(s) #这里注意要转换成字符串，ls转str可以用.join()方法
    
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        chars = list(s)
        
        while i < len(chars):
            chars[i:i + k] = chars[i:i + k][::-1] # 反转后，更改原值为反转后值
            i += k * 2

        return ''.join(chars)


if __name__ == "__main__":
    s = "abcdefg"
    k = 8
    so = Solution()
    print(so.reverseStr(list(s),k))
