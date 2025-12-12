#include "lc_pub.h"


class Solution {
    public:
    vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
        vector<int>ans(numberOfUsers, 0);
        vector<int>online(numberOfUsers, -1);
        ranges::sort(events, {}, [&](vector<string> ev) {return pair{stoi(ev[1]), ev[0][2]};});  // 按照时间戳从小到大排序，时间戳相同的，离线事件排在前面
        for (auto& ev: events) {
            if (ev[0] == "MESSAGE") {
                if (ev[2] == "ALL") {
                    for (int i=0;i<numberOfUsers;i++) {
                        ans[i]++;
                    }
                }
                else if (ev[2] == "HERE") {
                    for (int i=0;i<numberOfUsers;i++) {
                        if (online[i]<=stoi(ev[1]))
                            ans[i]++;
                    }
                }
                else {
                    for (const auto& part : ev[2] | ranges::views::split(' ')) {
                        string s(part.begin() + 2, part.end());
                        ans[stoi(s)]++;
                    }
                }
            }
            else {
                online[stoi(ev[2])]=stoi(ev[1])+60;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<string>> nums{{"MESSAGE","10","id1 id0"},{"OFFLINE","11","0"},{"MESSAGE","71","HERE"}};

    Solution so;
    cout << so.countMentions(2, nums) << endl;
    return 0;
}
