// 给你一个整数 n。

// 当存在 至少 两组不同的整数对 (a, b) 满足以下条件时，整数 x 被称为 好整数：

// a 和 b 是正整数。
// a <= b
// x = a3 + b3
// 返回一个数组，其中包含所有小于等于 n 的好整数，并按升序排序。

 

// 示例 1：

// 输入： n = 4104

// 输出： [1729,4104]

// 解释：

// 在小于等于 4104 的整数中，好整数包括：

// 1729：13 + 123 = 1729，以及 93 + 103 = 1729。
// 4104：23 + 163 = 4104，以及 93 + 153 = 4104。
// 因此，答案是 [1729, 4104]。

// 示例 2：

// 输入： n = 578

// 输出： []

// 解释：

// 不存在小于等于 578 的好整数，因此答案是空数组。

 

// 提示：

// 1 <= n <= 109

#include "lc_pub.h"

vector<unsigned int> cube;

auto init = [] {
    unordered_map<unsigned int,int>c;
    for (unsigned int i=1;i<=1000;i++)
        for (unsigned int j=i;j<=1000;j++) {
            int a=i*i*i,b=j*j*j;
            if (a+b>1e9) break;
            c[a+b]++;
            if (c[a+b]==2)
                cube.push_back(a+b);
        }
    // cout<<cube.size()<<endl;
    ranges::sort(cube);

    return 0;
}();

class Solution {
public:
    vector<int> findGoodIntegers(int n) {
        vector<int>ans;
        for (int x: cube) {
            if (x<=n) {
                ans.push_back(x);
            }
            else {
                break;
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-2,3,-4};

    Solution so;
    cout<<so.findGoodIntegers(1);
    return 0;
}
