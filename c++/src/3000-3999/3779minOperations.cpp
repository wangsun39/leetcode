// 给你一个整数数组 nums。

// 在一次操作中，你需要移除当前数组的 前三个元素。如果剩余元素少于三个，则移除 所有 剩余元素。

// 重复此操作，直到数组为空或不包含任何重复元素为止。

// 返回一个整数，表示所需的操作次数。

 

// 示例 1:

// 输入: nums = [3,8,3,6,5,8]

// 输出: 1

// 解释:

// 在第一次操作中，我们移除前三个元素。剩余的元素 [6, 5, 8] 互不相同，因此停止。仅需要一次操作。

// 示例 2:

// 输入: nums = [2,2]

// 输出: 1

// 解释:

// 经过一次操作后，数组变为空，满足停止条件。

// 示例 3:

// 输入: nums = [4,3,5,1,2]

// 输出: 0

// 解释:

// 数组中的所有元素都是互不相同的，因此不需要任何操作。

 

// 提示:

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 105

#include "lc_pub.h"

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n=nums.size();
        int m=(n+2)/3;
        unordered_set<int> us;
        int i=n-1;
        if (n%3==1) {
            us.insert(nums[n-1]);
            m-=1;
            i=n-2;
        }
        else if(n%3==2) {
            us.insert(nums[n-1]);
            if (nums[n-1]!=nums[n-2]) {
                us.insert(nums[n-2]);
            }
            else {
                return m;
            }
            i=n-3;
            m-=1;
        }
        for (;i>=0;i-=3) {
            int n1=us.size();
            us.insert(nums[i]);
            us.insert(nums[i-1]);
            us.insert(nums[i-2]);
            if (n1+3!=us.size()) {
                return m;
            }
            m-=1;
        }
        return m;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{100,4,13,12,92,25,23,63,38,82,15,19,74,85,56,13,13};

    Solution so;
    cout<<so.minOperations(nums);
    return 0;
}
