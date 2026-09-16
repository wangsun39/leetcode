// 给你一个整数 n，表示目标分数。

// 你的分数初始为 0，每天你既可以 获得 分数，也可以 跳过 。

// 分数是在连胜期间获得的。在连胜的第一天，你获得 1 分，第二天获得 2 分，第三天获得 3 分，依此类推。跳过 一天将获得 零分 并 重置 连胜，因此下一次你获得分数时，将再次从 1 开始。

// 返回达到 恰好 为 n 的分数所需的 最少 天数（包括所有跳过的天数）。

 

// 示例 1：

// 输入： n = 2

// 输出： 3

// 解释：

// 第 1 天：获得 1 分。分数为 1。
// 第 2 天：跳过，这会重置连胜。如果今天获得分数会加上 2 分，从而使分数超过 n = 2。
// 第 3 天：连胜已重置，因此获得 1 分。在 3 天内分数恰好达到 n = 2。
// 示例 2：

// 输入： n = 9

// 输出： 6

// 解释：

// 第 1 到 3 天：获得 1、2 和 3 分。分数为 1 + 2 + 3 = 6。
// 第 4 天：跳过，这会重置连胜。
// 第 5 和 6 天：获得 1 和 2 分。在 6 天内分数恰好达到 6 + 1 + 2 = 9。
// 示例 3：

// 输入： n = 12

// 输出： 7

// 解释：​​​​​​​

// 第 1 到 3 天：获得 1、2 和 3 分。分数为 1 + 2 + 3 = 6。
// 第 4 天：跳过，这会重置连胜。
// 第 5 到 7 天：获得 1、2 和 3 分。在 7 天内分数恰好达到 6 + 1 + 2 + 3 = 12。
 

// 提示：

// 1 <= n <= 105

#include "lc_pub.h"

#define MX 10000
vector<int> p0, p1;

auto init = [] {

    auto to_arr = [](int x, int arr[], int &len) -> void {
        int y=x;
        len=0;
        while (y) {
            arr[len] = y%10;
            len++;
            y/=10;
        }
        return ;
    };
    auto to_num = [](int arr[], int len) -> long long {
        long long res = 0;
        for (int i=0;i<len;i++) {
            res=res*10+arr[i];
        }
        return res;
    };

    p0.push_back(0);
    p1.push_back(0);
    for (int i=1;i<10;i++) {
        if (i%2)
            p1.push_back(i);
        else
            p0.push_back(i);
    }

    for (int j=1;j<MX;j++) {
        int s[11] = {0};
        int len;
        to_arr(j,s,len);
        for (int i=0;i<10;i++) {
            s[len]=i;
            for (int k=len+1;k<len*2+1;k++) {
                s[k]=s[len*2-k];
            }
            long long v=to_num(s, len*2+1);
            if (v%2)
                p1.push_back(v);
            else
                p0.push_back(v);
        }
        for (int k=len;k<len*2;k++) {
                s[k]=s[len*2-1-k];
            }
            long long v=to_num(s, len*2);
            if (v%2)
                p1.push_back(v);
            else
                p0.push_back(v);
    }
    p1.push_back(1'000'000'001);
    p0.push_back(2'000'000'002);
    ranges::sort(p1);
    ranges::sort(p0);
    
    return 0;
}();

class Solution {
public:
    long long minOperations(vector<int>& nums) {


        int n=nums.size();
        long long ans = 0;
        for (int i=0;i<n;i++) {
            long long v;
            if (nums[i]%2)
            {
                auto it=ranges::lower_bound(p1, nums[i]);
                v=min(nums[i]-*(it-1), *(it)-nums[i]);
            }
            else
            {
                auto it=ranges::lower_bound(p0, nums[i]);
                v=min(nums[i]-*(it-1), *(it)-nums[i]);
            }
                
            ans+=v/2;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{10,12,14,16};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.minOperations(nums)<<endl;
    return 0;
}
