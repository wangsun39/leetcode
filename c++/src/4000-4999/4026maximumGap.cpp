// 给你两个长度分别为 n 和 m 的字符串 skill 和 station。

// skill[i] 表示工人 i 的技能，station[j] 表示工位 j 所支持的技能。

// 你必须将每一名工人分配到一个互不相同的工位。令 ji 表示分配给工人 i 的工位下标。有效的分配方案必须满足：

// 对于每个 0 <= i < n，都有 station[ji] == skill[i]。
// 按照工人的顺序，分配的工位下标必须严格递增，即 j0 < j1 < ... < jn - 1。
// 分配方案的间隔是分配给两名相邻工人的工位下标之间的最大差值。换句话说，它等于所有 1 <= i < n 中 ji - ji - 1 的最大值。

// 如果只有一名工人，则间隔为 0。

// 返回所有有效分配方案中可能得到的最大间隔。题目保证至少存在一种有效的分配方案。

 

// 示例 1：

// 输入： skill = "aa", station = "aaaa"

// 输出： 3

// 解释：

// 必须将两名工人分配到两个不同的 'a' 工位。
// 将他们分配到工位 [0, 3]，得到的间隔为 3。
// 示例 2：

// 输入： skill = "xyz", station = "xyzz"

// 输出： 2

// 解释：

// 将工人 0 分配到工位 j = 0，将工人 1 分配到工位 j = 1。
// 为了最大化间隔，将工人 2 分配到工位 j = 3。
// 由此得到分配方案 [0, 1, 3]，相邻工位下标的差值为 [1, 2]，因此间隔为 2。
// 示例 3：

// 输入： skill = "cbc", station = "cbcdbc"

// 输出： 4

// 解释：

// 将工人 0 分配到工位 j = 0，将工人 1 分配到工位 j = 1。
// 为了最大化间隔，将工人 2 分配到工位 j = 5。
// 由此得到分配方案 [0, 1, 5]，相邻工位下标的差值为 [1, 4]，因此间隔为 4。
 

// 提示：

// skill.length == n
// station.length == m
// 1 <= n <= m <= 105
// skill 和 station 仅由小写英文字母组成。
// 题目保证所有工人都存在一种有效的分配方案。

#include "lc_pub.h"

class Solution {
public:
    int maximumGap(string skill, string station) {
        int n=skill.size(),m=station.size();
        vector<int>left(n,0),right(n,0);
        int j=0;
        for (int i=0;i<n;i++) {
            while (skill[i]!=station[j]) {
                j++;
            }
            left[i]=j;
            j++;
        }
        j=m-1;
        for (int i=n-1;i>=0;i--) {
            while (skill[i]!=station[j]) {
                j--;
            }
            right[i]=j;
            j--;
        }
        int ans=0;
        for (int i=0;i<n;i++) {
            if (i>0) {
                ans=max(ans,right[i]-left[i-1]);
                // ans=max(ans,right[i-1]-left[i]);
            }
            if (i<n-1) {
                ans=max(ans,right[i+1]-left[i]);
                // ans=max(ans,right[i]-left[i+1]);
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> pa{-1,0,0,0,2,2};
    vector<int> nums{5,2,3,1,4,6};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.maximumGap("xyz","xyzz");
    cout<<so.maximumGap("aa","aaaa");
    return 0;
}
