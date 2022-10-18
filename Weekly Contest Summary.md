| 时间 | 场次 | 题号 | 题目      | 难度 | 说明 |
|----|----|---------|-----|-----|--------|
|2022-10-16| 第315场周赛  | T4  | [对字母串可执行的最大删除数](https://leetcode.cn/problems/maximum-deletions-on-a-string/description/) |       | 本周前三题10分钟多点就完成了(wa了一次)，但这题又被卡住了，直到比赛结束后才做出来，感觉并不难，开始想去双指针，后来考虑分区间，最后还是用类似"以某个下标结尾的区间个数"进行统计的方法 |
|2022-10-2| 第313场周赛  | T3  | [最小 XOR](https://leetcode.cn/problems/minimize-xor/) |   1532    | 本周又是2000多名，哎。。。<br> 此题虽然做出来了，不过耽误了不少时间，方法有些复杂，可以参考excel中灵神的解法思路 |
|2022-10-2| 第313场周赛  | T4  | [对字母串可执行的最大删除数](https://leetcode.cn/problems/maximum-deletions-on-a-string/) |   2101    | 这题用了DFS+记忆化搜索，但TLE了 |
|2022-9-25| 第312场周赛  | T3  | [找到所有好下标](https://leetcode.cn/problems/find-all-good-indices/) |   1695    | 本周2400多名，创近两个月的最低记录<br> 这题考虑用单调栈，虽然也可以做出来，但写法复杂，比赛中没有写完。<br> 实际左右两次遍历就可以了 |
|2022-9-25| 第312场周赛  | T4  | [好路径的数目](https://leetcode.cn/problems/number-of-good-paths/) |   2444    | 这题难度较大，需要用到并查集，关键也不容易想到用并查集，并查集的模板需要继续练习 |
|2022-9-18| 第311场周赛  | T4  | [字符串的前缀分数和](https://leetcode.cn/problems/sum-of-prefix-scores-of-strings/) |  1725     | 本周AK，排名不高。<br> 这次就靠暴力哈希过的。另外Trie树的方法，值得保存一个模板 |
|2022-9-11| 第310场周赛  | T4  | [最长递增子序列 II](https://leetcode.cn/problems/longest-increasing-subsequence-ii/) |   2280    | 没做出来，本以为最长递增子序是按DP来计算的，没想到需要用线段树<br> 在求解「上升子序列」问题时，期望O(NlogN)的复杂度，一般有两种优化方法：单调栈 + 二分优化；线段树、平衡树等数据结构优化。 |
|2022-9-4| 第309场周赛  | T4  | [会议室 III](https://leetcode.cn/problems/meeting-rooms-iii/) |   2092    | 排序 + 优先队列，比赛结束后5分钟做完了，有点可惜，但也是参考了会议室 II的思路 |
|2022-8-28| 第308场周赛  | T4  | [给定条件下构造矩阵](https://leetcode.cn/problems/build-a-matrix-with-conditions/) |   1960    | 没能做出来，感觉就差一点了，拓扑排序之前没有关注过，需要多练习此方法<br>本周前三题做的比较顺，18分钟，可惜最后一题了 |
|2022-8-21| 第307场周赛  | T4  | [找出数组的第 K 大和](https://leetcode.cn/problems/find-the-k-sum-of-an-array/) |   2647    | 本周周赛，第一题被卡了快半小时，差点要放弃比赛了，后来还算坚持下来，做出来3题，就是速度有点慢。第四题难度太大放弃了 |
|2022-8-14| 第306场周赛  | T4  | [统计特殊整数](https://leetcode.cn/problems/count-special-integers/) |   2120    | 数位DP，没做出来，灵神总结了一个模块，已经记录下来<br>此题之前leetcode有个及其相似的题(1012)，比赛的时候已经看到有人提到了，也看到了答案，但还是忍住了没有抄答案。<br>虽然leetcode不应该这么出题，估计不少人都是抄了答案提交的，但还是技不如人，继续加油吧，&#x1F337; |
|2022-8-7| 第305场周赛  | T4  | [最长理想子序列](https://leetcode.cn/problems/longest-ideal-subsequence/) |   1834    | 26个字母的DP， 每周AK(796) |
|2022-7-31| 第304场周赛  | T2  | [分组的最大数量](https://leetcode.cn/problems/maximum-number-of-groups-entering-a-competition/) |   1502    | 小技巧，其实和数组元素无关 |
|2022-7-31| 第304场周赛  | T4  | [图中的最长环](https://leetcode.cn/problems/longest-cycle-in-a-graph/) |    1897   | 本周AK(430) |
|2022-7-24| 第303场周赛  | T4  | [优质数对的数目](https://leetcode.cn/problems/minimum-deletions-to-make-array-divisible/) |  2075     | 一道涉及位运算的题，要用到公式： (A & B).bit_counter() + (A \| B).bit_counter() == A.bit_count() + B.bit_count() 有一定的技巧 |
|2022-7-17| 第302场周赛  | T4  | [使数组可以被整除的最少删除次数](https://leetcode.cn/problems/number-of-excellent-pairs/submissions/) |  1651     | GCD  |
|2022-7-10| 第301场周赛  | T1  | [装满杯子需要的最短总时长](https://leetcode.cn/problems/minimum-amount-of-time-to-fill-cups/) |  1360     | 需要有点数学技巧：<br>假设amount中三个数从小到大依次为n1 <= n2 <= n3，<br>1) 如果n3 >= n1 + n2,那么结果就是n3.<br>2) 否则，可以证明，答案能达到下界sum(amount)/2上取整  |
|2022-7-10| 第301场周赛  | T4  | [统计理想数组的数目](https://leetcode.cn/problems/count-the-number-of-ideal-arrays/) |  2615     | 难度很大，用到了排列组合的数学知识，再加上一些编程技巧  |
|2022-7-3| 第300场周赛  | T2  | [螺旋矩阵 IV](https://leetcode.cn/problems/spiral-matrix-iv/) |    1421   | 题目本身不涉及高级的算法<br>但有点繁琐，花了太多时间&#x1F622;，<br>其实可以参考一下之前类似的题目的（I/II/III） |
|2022-7-3| 第300场周赛  | T3  | [知道秘密的人数](https://leetcode.cn/problems/number-of-people-aware-of-a-secret/) |   1893    | 比较标准的DP，两个递推公式<br>由于前一题花了1个多小时，导致这题没做完&#x1F639; |
|2022-7-3| 第300场周赛  | T4  | [网格图中递增路径的数目](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) |   2001    | DFS<br>之前类似的题目 [329](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) |
