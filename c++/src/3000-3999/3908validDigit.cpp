// 给你一个整数 n 和一个数字 x。

// 如果一个数字满足以下条件，则认为它是 有效 的：

// 它包含 至少一个 数字 x，并且
// 它 不以 数字 x 开头。
// 如果 n 是 有效 的，请返回 true，否则返回 false。

 

// 示例 1：

// 输入： n = 101, x = 0

// 输出： true

// 解释：

// 该数字在下标 1 处包含数字 0。它不以 0 开头，因此满足两个条件。所以，答案是 true。

// 示例 2：

// 输入： n = 232, x = 2

// 输出： false

// 解释：

// 该数字以 2 开头，违反了条件。所以，答案是 false。

// 示例 3：

// 输入： n = 5, x = 1

// 输出： false

// 解释：

// 该数字不包含数字 1。所以，答案是 false。

 

// 提示：

// 0 <= n <= 105
// 0 <= x <= 9

#include "lc_pub.h"

class Solution {
public:
    bool validDigit(int n, int x) {
        vector<int> arr;
        bool exist=false;
        while (n) {
            if (n%10==x) exist=true;
            arr.push_back(n%10);
            n/=10;
        }
        int m=arr.size();
        if (m&&arr[m-1]!=x&&exist) {
            return true;
        }
        return false;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4};

    Solution so;
    return 0;
}
