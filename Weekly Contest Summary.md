| 时间 | 场次 | 题号 | 题目      | 难度 | 说明 |
|----|----|---------|-----|-----|--------|
|2023-1-8| 第327场周赛  | Q3  | [使字符串总不同字符的数目相等](https://leetcode.cn/problems/make-number-of-distinct-characters-equal/) |   1776    | 这题在比赛中花了近一个小时，WA了3次，考虑分类讨论，想的复杂了。4分的难度不应该想的太复杂 |
|2023-1-8| 第327场周赛  | Q4  | [过桥的时间](https://leetcode.cn/problems/time-to-cross-a-bridge/) |   2589    | 比赛中时间太少没能做出来，赛后，花了1-2个小时独立完成，这题是模拟类型的题，比较繁琐，要考虑好如何建模 |
|2023-1-1| 第326场周赛  | Q4  | [范围内最接近的两个质数](https://leetcode.cn/problems/closest-prime-numbers-in-range/) |   1649    | 本周AK，素数的判断出现在两道题上，比赛时参考了网上的埃氏筛，后来从灵神的视频中了解了欧拉筛，可以总结一下素数的模板 |
|2022-12-25| 第325场周赛  | Q3  | [礼盒的最大甜蜜度](https://leetcode.cn/problems/maximum-tastiness-of-candy-basket/) |    2021   | 本周除了第一题，都有难度。差点第二题都没做完，外加身体还没恢复（&#x1F637;, 当然恢复了，估计这题也做不出来） <br> 这题正着想很难，需要逆向思考，然后用二分就比较容易了 |
|2022-12-25| 第325场周赛  | Q4  | [好分区的数目](https://leetcode.cn/problems/number-of-great-partitions/) |   2415    | 这题同样是计算不满足的组合数，再用总数减，外带DP  |
|2022-12-18| 第324场周赛  | Q3  | [添加边使所有节点度数都为偶数](https://leetcode.cn/problems/add-edges-to-make-degrees-of-all-nodes-even/) |   2060    | 本周AK，WA 3次 <br>总体上说难度不是很大，但3,4两题各掉到一个坑里去了  |
|2022-12-18| 第324场周赛  | Q4  | [查询树中环的长度](https://leetcode.cn/problems/cycle-length-queries-in-a-tree/) |   1948    | LCA  |
|2022-12-11| 第323场周赛  | Q4  | [矩阵查询可获得的最大分数](https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/) |    2195   | 本周AK，没有WA <br>对查询数组进行排序，对每个查询跑一下BFS，就可以避免重复计算 <br>其他方法，可以用更好的方法：并查集  |
|2022-12-4| 第322场周赛  | Q4  | [将节点分成尽可能多的组](https://leetcode.cn/problems/divide-nodes-into-the-maximum-number-of-groups/) |    2415   | 本周前三题WA了一次，大概半小时完成<br>然后就进入垃圾时间了，实际当时理解题目也有问题，\|y - x\| = 1，看成了\|y - x\| <= 1。总之，这题难度有点大了 |
|2022-11-27| 第321场周赛  | Q4  | [统计中位数为 K 的子数组](https://leetcode.cn/problems/count-subarrays-with-median-k/) |    1998   | 本周AK<br>前三题比较顺利。这题想了一会儿，最后考虑采用中心向左右拓展计算 (大于的元素个数-小于的元素个数) 的方法，再用哈希 |
|2022-11-20| 第320场周赛  | Q2  | [二叉搜索树最近节点查询](https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/) |  1596     | 本周Q2 Q4都没完成，这题本来不难，想到了思路，先中序遍历，再二分查找，<br>但中序遍历的DFS，复杂度是O(n^2)，python的这种中序遍历法还是要注意。 |
|2022-11-20| 第320场周赛  | Q4  | [完美分割的方案数](https://leetcode.cn/problems/number-of-beautiful-partitions/) |  2344     | 第四题比赛时，没有时间看，时间都耗在Q2上了。赛后思考，也想到了DP的方法，但复杂度是O(n^3)，还需要加一个前缀和的优化步骤，这题还是比较难的 |
|2022-11-13| 第319场周赛  | Q4  | [不重叠回文子字符串的最大数目](https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/) |   2013    | 本周和上次情况类似，前三题做完基本到时间了，<br>第二题wa了2次，花了差不多1小时，又是想歪了。<br> 第四题需要用的DP，以及求出所有回文子串的方法：中心拓展法，之前有些类似的题目，[132](https://leetcode.cn/problems/palindrome-partitioning-ii/)、[647](https://leetcode.cn/problems/palindromic-substrings/)<br>目前的一个问题：会做的题不能快速做出来。 |
|2022-11-6| 第318场周赛  | Q4  | [最小移动总距离](https://leetcode.cn/problems/minimum-total-distance-traveled/) |   2453    | 本周前三题虽然做出来了，但花了很多时间1:12:36，最后一题本来就难，更是没时间做出来了<br>第二题开始想到双指针去了，耽误了不少时间，<br>第三题wa了3次 |
|2022-10-30| 第317场周赛  | Q4  | [移除子树后的二叉树高度](https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/) |   2298    | 本周AK &#x1F603;，这题wa了4次，总是TLE，最后发现是list开的太大了，还好提前几分钟过了 |
|2022-10-30| 第316场周赛  | Q3  | [使数组相等的最小开销](https://leetcode.cn/problems/minimum-cost-to-make-array-equal/description/) |   2005    | 这题又是属于比赛时已经有思路了，但是没能调试出来，导致本周只做了2题，还是不够熟练。<br> 当然方法也是可以优化一点，最优值一点在数组的某个值上取到 |
|2022-10-23| 第316场周赛  | Q4  | [使数组相似的最少操作次数](https://leetcode.cn/problems/minimum-number-of-operations-to-make-arrays-similar/) |    2076   | 因为第三题耗时太长，这题没有时间做，当然第三题没耽误，这题也不一定做出来。技巧：奇偶分类，可以把奇数取相反数，这样它们就分开了。<br>这题和第三题是有点像的。 |
|2022-10-16| 第315场周赛  | Q4  | [对字母串可执行的最大删除数](https://leetcode.cn/problems/maximum-deletions-on-a-string/description/) |    2092   | 本周前三题10分钟多点就完成了(wa了一次)，但这题又被卡住了，直到比赛结束后才做出来，感觉并不难，开始想去双指针，后来考虑分区间，最后还是用类似"以某个下标结尾的区间个数"进行统计的方法 |
|2022-10-2| 第313场周赛  | Q3  | [最小 XOR](https://leetcode.cn/problems/minimize-xor/) |   1532    | 本周又是2000多名，哎。。。<br> 此题虽然做出来了，不过耽误了不少时间，方法有些复杂，可以参考excel中灵神的解法思路 |
|2022-10-2| 第313场周赛  | Q4  | [对字母串可执行的最大删除数](https://leetcode.cn/problems/maximum-deletions-on-a-string/) |   2101    | 这题用了DFS+记忆化搜索，但TLE了 可以用LCP + 逆序DP|
|2022-9-25| 第312场周赛  | Q3  | [找到所有好下标](https://leetcode.cn/problems/find-all-good-indices/) |   1695    | 本周2400多名，创近两个月的最低记录<br> 这题考虑用单调栈，虽然也可以做出来，但写法复杂，比赛中没有写完。<br> 实际左右两次遍历就可以了 |
|2022-9-25| 第312场周赛  | Q4  | [好路径的数目](https://leetcode.cn/problems/number-of-good-paths/) |   2444    | 这题难度较大，需要用到并查集，关键也不容易想到用并查集，并查集的模板需要继续练习 |
|2022-9-18| 第311场周赛  | Q4  | [字符串的前缀分数和](https://leetcode.cn/problems/sum-of-prefix-scores-of-strings/) |  1725     | 本周AK，排名不高。<br> 这次就靠暴力哈希过的。另外Trie树的方法，值得保存一个模板 |
|2022-9-11| 第310场周赛  | Q4  | [最长递增子序列 II](https://leetcode.cn/problems/longest-increasing-subsequence-ii/) |   2280    | 没做出来，本以为最长递增子序是按DP来计算的，没想到需要用线段树<br> 在求解「上升子序列」问题时，期望O(NlogN)的复杂度，一般有两种优化方法：单调栈 + 二分优化；线段树、平衡树等数据结构优化。 |
|2022-9-4| 第309场周赛  | Q4  | [会议室 III](https://leetcode.cn/problems/meeting-rooms-iii/) |   2092    | 排序 + 优先队列，比赛结束后5分钟做完了，有点可惜，但也是参考了会议室 II的思路 |
|2022-8-28| 第308场周赛  | Q4  | [给定条件下构造矩阵](https://leetcode.cn/problems/build-a-matrix-with-conditions/) |   1960    | 没能做出来，感觉就差一点了，拓扑排序之前没有关注过，需要多练习此方法<br>本周前三题做的比较顺，18分钟，可惜最后一题了 |
|2022-8-21| 第307场周赛  | Q4  | [找出数组的第 K 大和](https://leetcode.cn/problems/find-the-k-sum-of-an-array/) |   2647    | 本周周赛，第一题被卡了快半小时，差点要放弃比赛了，后来还算坚持下来，做出来3题，就是速度有点慢。第四题难度太大放弃了 |
|2022-8-14| 第306场周赛  | Q4  | [统计特殊整数](https://leetcode.cn/problems/count-special-integers/) |   2120    | 数位DP，没做出来，灵神总结了一个模块，已经记录下来<br>此题之前leetcode有个及其相似的题(1012)，比赛的时候已经看到有人提到了，也看到了答案，但还是忍住了没有抄答案。<br>虽然leetcode不应该这么出题，估计不少人都是抄了答案提交的，但还是技不如人，继续加油吧，&#x1F337; |
|2022-8-7| 第305场周赛  | Q4  | [最长理想子序列](https://leetcode.cn/problems/longest-ideal-subsequence/) |   1834    | 26个字母的DP， 每周AK(796) |
|2022-7-31| 第304场周赛  | Q2  | [分组的最大数量](https://leetcode.cn/problems/maximum-number-of-groups-entering-a-competition/) |   1502    | 小技巧，其实和数组元素无关 |
|2022-7-31| 第304场周赛  | Q4  | [图中的最长环](https://leetcode.cn/problems/longest-cycle-in-a-graph/) |    1897   | 本周AK(430) |
|2022-7-24| 第303场周赛  | Q4  | [优质数对的数目](https://leetcode.cn/problems/minimum-deletions-to-make-array-divisible/) |  2075     | 一道涉及位运算的题，要用到公式： (A & B).bit_counter() + (A \| B).bit_counter() == A.bit_count() + B.bit_count() 有一定的技巧 |
|2022-7-17| 第302场周赛  | Q4  | [使数组可以被整除的最少删除次数](https://leetcode.cn/problems/number-of-excellent-pairs/submissions/) |  1651     | GCD  |
|2022-7-10| 第301场周赛  | T1  | [装满杯子需要的最短总时长](https://leetcode.cn/problems/minimum-amount-of-time-to-fill-cups/) |  1360     | 需要有点数学技巧：<br>假设amount中三个数从小到大依次为n1 <= n2 <= n3，<br>1) 如果n3 >= n1 + n2,那么结果就是n3.<br>2) 否则，可以证明，答案能达到下界sum(amount)/2上取整  |
|2022-7-10| 第301场周赛  | Q4  | [统计理想数组的数目](https://leetcode.cn/problems/count-the-number-of-ideal-arrays/) |  2615     | 难度很大，用到了排列组合的数学知识，再加上一些编程技巧  |
|2022-7-3| 第300场周赛  | Q2  | [螺旋矩阵 IV](https://leetcode.cn/problems/spiral-matrix-iv/) |    1421   | 题目本身不涉及高级的算法<br>但有点繁琐，花了太多时间&#x1F622;，<br>其实可以参考一下之前类似的题目的（I/II/III） |
|2022-7-3| 第300场周赛  | Q3  | [知道秘密的人数](https://leetcode.cn/problems/number-of-people-aware-of-a-secret/) |   1893    | 比较标准的DP，两个递推公式<br>由于前一题花了1个多小时，导致这题没做完&#x1F639; |
|2022-7-3| 第300场周赛  | Q4  | [网格图中递增路径的数目](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) |   2001    | DFS<br>之前类似的题目 [329](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) |
