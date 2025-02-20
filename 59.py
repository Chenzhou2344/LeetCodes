class Solution(object):
    def generateMatrix(self, n):
        if n <= 0:
            return []
        
        # 初始化 n x n 矩阵
        matrix = [[0]*n for _ in range(n)]

        # 初始化边界和起始值
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1

        while top <= bottom and left <= right:
            # 从左到右填充上边界
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # 从上到下填充右边界
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # 从右到左填充下边界

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            # 从下到上填充左边界

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix

if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3)) # [[1,2,3],[2,4,6],[3,6,9]]
    print(s.generateMatrix(1)) # [[1]]
    print(s.generateMatrix(4)) # [[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]