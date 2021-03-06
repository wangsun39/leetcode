| 时间 | 场次 | 题号 | 题目      | 难度 | 说明 |
|----|----|---------|-----|-----|--------|
|2022-7-31| 第304场周赛  | T2  | [分组的最大数量](https://leetcode.cn/problems/maximum-number-of-groups-entering-a-competition/) |       | 小技巧，其实和数组元素无关 |
|2022-7-31| 第304场周赛  | T4  | [图中的最长环](https://leetcode.cn/problems/longest-cycle-in-a-graph/) |       | 本周AK |
|2022-7-24| 第303场周赛  | T4  | [优质数对的数目](https://leetcode.cn/problems/minimum-deletions-to-make-array-divisible/) |  2075     | 一道涉及位运算的题，要用到公式： (A & B).bit_counter() + (A \| B).bit_counter() == A.bit_count() + B.bit_count() 有一定的技巧 |
|2022-7-17| 第302场周赛  | T4  | [使数组可以被整除的最少删除次数](https://leetcode.cn/problems/number-of-excellent-pairs/submissions/) |  1651     | GCD  |
|2022-7-10| 第301场周赛  | T1  | [装满杯子需要的最短总时长](https://leetcode.cn/problems/minimum-amount-of-time-to-fill-cups/) |  1360     | 需要有点数学技巧：<br>假设amount中三个数从小到大依次为n1 <= n2 <= n3，<br>1) 如果n3 >= n1 + n2,那么结果就是n3.<br>2) 否则，可以证明，答案能达到下界sum(amount)/2上取整  |
|2022-7-10| 第301场周赛  | T4  | [统计理想数组的数目](https://leetcode.cn/problems/count-the-number-of-ideal-arrays/) |  2615     | 难度很大，用到了排列组合的数学知识，再加上一些编程技巧  |
|2022-7-3| 第300场周赛  | T2  | [螺旋矩阵 IV](https://leetcode.cn/problems/spiral-matrix-iv/) |    1421   | 题目本身不涉及高级的算法<br>但有点繁琐，花了太多时间&#x1F622;，<br>其实可以参考一下之前类似的题目的（I/II/III） |
|2022-7-3| 第300场周赛  | T3  | [知道秘密的人数](https://leetcode.cn/problems/number-of-people-aware-of-a-secret/) |   1893    | 比较标准的DP，两个递推公式<br>由于前一题花了1个多小时，导致这题没做完&#x1F639; |
|2022-7-3| 第300场周赛  | T4  | [网格图中递增路径的数目](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) |   2001    | DFS<br>之前类似的题目 [329](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) |
