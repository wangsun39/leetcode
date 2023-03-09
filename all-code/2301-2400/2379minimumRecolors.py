# 给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。
#
# 给你一个整数 k ，表示想要 连续 黑色块的数目。
#
# 每一次操作中，你可以选择一个白色块将它 涂成 黑色块。
#
# 请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。
#
#
#
# 示例 1：
#
# 输入：blocks = "WBBWWBBWBW", k = 7
# 输出：3
# 解释：
# 一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
# 得到 blocks = "BBBBBBBWBW" 。
# 可以证明无法用少于 3 次操作得到 7 个连续的黑块。
# 所以我们返回 3 。
# 示例 2：
#
# 输入：blocks = "WBWBBBW", k = 2
# 输出：0
# 解释：
# 不需要任何操作，因为已经有 2 个连续的黑块。
# 所以我们返回 0 。
#
#
# 提示：
#
# n == blocks.length
# 1 <= n <= 100
# blocks[i] 要么是 'W' ，要么是 'B' 。
# 1 <= k <= n

from collections import Counter


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter = Counter(blocks[:k])
        ans = counter['W']
        for i, x in enumerate(blocks[k:], k):
            counter[blocks[i - k]] -= 1
            counter[x] += 1
            ans = min(ans, counter['W'])
        return ans


so = Solution()
print(so.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))
print(so.minimumRecolors(blocks = "WBWBBBW", k = 2))




