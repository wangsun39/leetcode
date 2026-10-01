// 给你一个整数数组 nums。

// 初始时，你有一个 空 数组 ans。重复执行以下操作，直到 nums 变为 空 ：

// 找出当前 nums 中 所有不同 的值。
// 将当前 nums 中每个 不同 的值各移除一个，并按 升序 将这些值依次添加到 ans 中。
// 返回数组 ans。

 

// 示例 1：

// 输入： nums = [3,1,3,2,1,3]

// 输出： [1,2,3,1,3,3]

// 解释：

// 操作	添加到 ans 的值	操作后的 nums	操作后的 ans
// 1	1, 2, 3	[3, 1, 3]	[1, 2, 3]
// 2	1, 3	[3]	[1, 2, 3, 1, 3]
// 3	3	[]	[1, 2, 3, 1, 3, 3]
// 此时 nums 已为空，因此答案为 [1, 2, 3, 1, 3, 3]。

// 示例 2：

// 输入： nums = [7,7,4,4,4]

// 输出： [4,7,4,7,4]

// 解释：

// 操作	添加到 ans 的值	操作后的 nums	操作后的 ans
// 1	4, 7	[7, 4, 4]	[4, 7]
// 2	4, 7	[4]	[4, 7, 4, 7]
// 3	4	[]	[4, 7, 4, 7, 4]
// 此时 nums 已为空，因此答案为 [4, 7, 4, 7, 4]。

 

// 提示：

// 1 <= nums.length <= 100
// 1 <= nums[i] <= 100

#include "lc_pub.h"

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        unordered_map<int,int>counter;
        for (int x: nums) {
            counter[x]++;
        }
        vector<int>keys;
        for (auto &[k,v]: counter) {
            keys.push_back(k);
        }
        ranges::sort(keys);
        int n=nums.size();
        int j=0,m=keys.size();
        vector<int>ans(n,0);
        for (int i=0;i<n;i++) {
            while (0==counter[keys[j]]) {
                j++;
                j%=m;
            }
            ans[i]=keys[j];
            counter[keys[j]]--;
            j++;
            j%=m;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{7,7,3,3};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.rearrangeArray(nums)<<endl;
    return 0;
}
