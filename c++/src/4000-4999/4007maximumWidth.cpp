// 给你一个整数数组 planks，其中 planks[i] 表示第 i 块木板的高度。每块木板的宽度为 1 个单位。

// 你想要用木板建造一个栅栏，栅栏中的所有木板必须具有 相同 的高度。

// 你可以直接使用原本的木板，或者将两块不同的原始木板组合成一块新木板，其高度 等于 这两块木板的高度之和。每块原始木板 最多 只能使用一次，并且不需要使用所有的原始木板。

// 返回可以建造的栅栏的 最大可能宽度。

 

// 示例 1：

// 输入： planks = [1,3,2,5,7,5,4,2,1]

// 输出： 4

// 解释：

// 我们可以得到四块高度为 5 的木板。

// planks[3] = 5
// planks[5] = 5
// planks[0] + planks[6] = 1 + 4 = 5
// planks[1] + planks[2] = 3 + 2 = 5
// 因此，最大宽度为 4。

// 示例 2：

// 输入： planks = [2,3,7]

// 输出： 1

// 解释：

// 即使组合两块不同的原始木板，也不可能形成两块高度相同的木板。
// 由于不需要使用所有的原始木板，我们可以选择任意一块木板作为栅栏。
// 因此，最大可能宽度为 1。
 

// 提示：

// 1 <= planks.length <= 1000
// 1 <= planks[i] <= 109

#include "lc_pub.h"

class Solution {
public:
    int maximumWidth(vector<int>& planks) {
        unordered_map<int,int>c1;
        unordered_map<int,int>c2;
        vector<int> s;
        int n=planks.size(),ans=1;
        for (int i=0;i<n;i++) {
            c1[planks[i]]+=1;
        }
        for (auto [k, v]: c1) {
            s.push_back(k);
        }
        int m=s.size();

        for (int i=0;i<m;i++) {
            int h=s[i]*2;
            c2[h]+=c1[s[i]]/2;
            c2[s[i]]+=c1[s[i]];
            for (int j=i+1;j<m;j++) {
                int h=s[i]+s[j];
                c2[h]+=min(c1[s[i]], c1[s[j]]);
            }
        }
        for (auto &[h, v]: c2) {
            ans=max(ans, v);
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr{39,14,56,96,55,56,83,38,33,27,98,71,68,1,42,31,14,42,34,23,68,81,56,33,56,59,71,59,81,56,80,15,28,42,28,56,46,46,42,14,23,72,19,6,81,56,71,56,33,58};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.maximumWidth(arr);
    return 0;
}
