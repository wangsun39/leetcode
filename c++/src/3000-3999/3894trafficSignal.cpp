// 给你一个整数 timer，表示交通信号灯上的剩余时间（以秒为单位）。

// 信号灯遵循以下规则：

// 如果 timer == 0，信号灯为 "Green"
// 如果 timer == 30，信号灯为 "Orange"
// 如果 30 < timer <= 90，信号灯为 "Red"
// 返回信号灯的当前状态。如果均不满足上述条件，返回 "Invalid"。

 

// 示例 1：

// 输入： timer = 60

// 输出： "Red"

// 解释：

// 因为 timer = 60，且 30 < timer <= 90，所以答案是 "Red"。

// 示例 2：

// 输入： timer = 5

// 输出： "Invalid"

// 解释：

// 因为 timer = 5，不满足任何给定的条件，所以答案是 "Invalid"。

 

// 提示：

// 0 <= timer <= 1000

#include "lc_pub.h"

class Solution {
public:
    string trafficSignal(int timer) {
        if (timer==30) return "Orange";
        if (timer==0) return "Green";
        if (timer>30&&timer<=90) return "Red";
        return "Invalid";
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-2,3,-4};

    Solution so;
    return 0;
}
