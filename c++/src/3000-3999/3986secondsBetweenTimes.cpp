// 给你两个有效时间 startTime 和 endTime，它们均以字符串形式表示，格式为 "HH:MM:SS"。

// 返回从 startTime 到 endTime 经过的秒数（包含两个端点）。

 

// 示例 1：

// 输入： startTime = "01:00:00", endTime = "01:00:25"

// 输出： 25

// 解释：

// endTime 比 startTime 晚 25 秒。

// 示例 2：

// 输入： startTime = "12:34:56", endTime = "13:00:00"

// 输出： 1504

// 解释：

// endTime 比 startTime 晚 25 分 4 秒，共计 1504 秒。

 

// 提示：

// startTime.length == 8
// endTime.length == 8
// startTime 和 endTime 均为格式 "HH:MM:SS" 的有效时间
// 00 <= HH <= 23
// 00 <= MM <= 59
// 00 <= SS <= 59
// endTime 不早于 startTime

#include "lc_pub.h"

class Solution {
public:
    int secondsBetweenTimes(string startTime, string endTime) {
        int h1=(startTime[0]-'0') * 10 + startTime[1]-'0';
        int m1=(startTime[3]-'0') * 10 + startTime[4]-'0';
        int s1=(startTime[6]-'0') * 10 + startTime[7]-'0';
        int h2=(endTime[0]-'0') * 10 + endTime[1]-'0';
        int m2=(endTime[3]-'0') * 10 + endTime[4]-'0';
        int s2=(endTime[6]-'0') * 10 + endTime[7]-'0';

        int ans = 0;
        if (s2>=s1) ans+=s2-s1;
        else {
            ans+=s2-s1+60;
            if(m2)m2-=1;
            else {
                m2=59;
                h2--;
            }
        }
        if (m2>=m1) ans+=(m2-m1)*60;
        else {
            ans+=(m2-m1)*60+3600;
            h2-=1;
        }
        ans+=(h2-h1)*3600;
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{0,0,0,2,0};
    // auto items=parseGrid("[[6,2],[2,6],[3,4]]");
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
