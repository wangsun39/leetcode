// 给你三个整数数组 types、colors 和 groupSize，其中 types 和 colors 的长度为 n，groupSize 的长度为 m。

// types[i] 表示下标 i 处元素的类型。
// colors[i] 表示下标 i 处元素的颜色。
// groupSize[t] 表示类型为 t 的删除组需要的元素数量。
// 在一次操作中，如果 恰好 groupSize[t] 个 连续 元素都具有类型 t 且颜色 相同 ，你可以将它们移除。

// 在每次移除后，剩余的元素会重新 相邻 ，同时保持它们的相对顺序。

// 如果可以通过一系列有效操作移除所有元素，返回 true。否则，返回 false。

 

// 示例 1：

// 输入： types = [0,1,1,0], colors = [5,3,3,5] , groupSize = [2,2]

// 输出： true

// 解释：

// 首先，移除下标 1 和 2 处的连续元素。这两个元素的类型均为 1，颜色均为 3，且组大小等于 groupSize[1] = 2。
// 剩余的序列为：types = [0, 0]，colors = [5, 5]
// 现在移除剩下的两个元素。它们的类型为 0，颜色为 5，且组大小等于 groupSize[0] = 2。
// 所有元素已被移除，因此答案是 true。
// 示例 2：

// 输入： types = [0,1,0], colors = [9,9,9], groupSize = [3,2]

// 输出： false

// 解释：

// 无法执行任何有效操作，因为没有一个连续组满足其所需的大小。
// 因此，无法移除所有元素，所以答案是 false。
// 示例 3：

// 输入： types = [2,0,1,2], colors = [7,5,4,7], groupSize = [3,1,2]

// 输出： false

// 解释：

// 移除下标 2 处的元素。它的类型为 1，颜色为 4，并形成一个大小为 groupSize[1] = 1 的连续组。
// 剩余的序列为：types = [2, 0, 2]，colors = [7, 5, 7]。
// 无法再执行进一步的操作，因此答案是 false。
 

// 提示：

// 1 <= n == types.length == colors.length <= 105
// 1 <= m == groupSize.length <= 105
// 0 <= types[i] <= m - 1
// 1 <= colors[i] <= 105
// 1 <= groupSize[t] <= n



#include "lc_pub.h"

class Solution {
public:
    bool canRemoveAll(vector<int>& types, vector<int>& colors, vector<int>& groupSize) {
        stack<vector<int>> st;
        int n=types.size();
        for (int i=0;i<n;i++) {
            if (st.size()) {
                int j=st.top()[0];
                int &m=st.top()[1];
                if (types[j]==types[i]&&colors[j]==colors[i]) {
                    if (m+1==groupSize[types[j]]) {
                        st.pop();
                    }
                    else {
                        m++;
                    }
                }
                else {
                    if (groupSize[types[i]]>1)
                        st.push({i, 1});
                }
            }
            else {
                if (groupSize[types[i]]>1)
                    st.push({i, 1});
            }
        }
        return st.size()==0;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{0,1,0},col={9,9,9},grp={1,1};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");
    Solution so;
    cout<<so.canRemoveAll(nums,col,grp)<<endl;

    return 0;
}
