// 给你一个字符串数组 events。

// 一开始，score = 0 且 counter = 0。events 中的每个元素为以下之一：

// "0", "1", "2", "3", "4", "6"：将该值加到总得分中。
// "W"：计数器加 1。不增加得分。
// "WD"：总得分加 1。
// "NB"：总得分加 1。
// 从左到右处理数组。当满足以下任一条件时停止处理：

// events 中的所有元素都已处理完毕，或
// 计数器变为 10。
// 返回一个整数数组 [score, counter]，其中：

// score 是最终的总得分。
// counter 是最终的计数器值。
 

// 示例 1：

// 输入： events = ["1","4","W","6","WD"]

// 输出： [12,1]

// 解释：

// 事件	得分	计数器
// "1"	1	0
// "4"	5	0
// "W"	5	1
// "6"	11	1
// "WD"	12	1
// 最终结果：[12, 1]。

// 示例 2：

// 输入： events = ["WD","NB","0","4","4"]

// 输出： [10,0]

// 解释：

// 事件	得分	计数器
// "WD"	1	0
// "NB"	2	0
// "0"	2	0
// "4"	6	0
// "4"	10	0
// 最终结果：[10, 0]。

// 示例 3：

// 输入： events = ["W","W","W","W","W","W","W","W","W","W","W"]

// 输出： [0,10]

// 解释：

// 出现 10 次 "W" 后，计数器达到 10，因此停止处理。剩余的事件将被忽略。

 

// 提示：

// 1 <= events.length <= 1000
// events[i] 是 "0"、"1"、"2"、"3"、"4"、"6"、"W"、"WD" 或 "NB" 之一。

#include "lc_pub.h"

class Solution {
public:
    vector<int> scoreValidator(vector<string>& events) {
        int score=0,counter=0;
        for (auto &e: events) {
            if (e[0]>='0'&&e[0]<='6') score+=e[0]-'0';
            else if(e.size()==2) score++;
            else counter++;
            if (counter==10) break;
        }
        return  {score, counter};
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4};

    Solution so;
    return 0;
}
