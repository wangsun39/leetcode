#include "lc_pub.h"

// 给你一个下标从 0 开始的正整数数组 tasks ，表示需要 按顺序 完成的任务，其中 tasks[i] 表示第 i 件任务的 类型 。

// 同时给你一个正整数 space ，表示一个任务完成 后 ，另一个 相同 类型任务完成前需要间隔的 最少 天数。

// 在所有任务完成前的每一天，你都必须进行以下两种操作中的一种：

// 完成 tasks 中的下一个任务
// 休息一天
// 请你返回完成所有任务所需的 最少 天数。

 

// 示例 1：

// 输入：tasks = [1,2,1,2,3,1], space = 3
// 输出：9
// 解释：
// 9 天完成所有任务的一种方法是：
// 第 1 天：完成任务 0 。
// 第 2 天：完成任务 1 。
// 第 3 天：休息。
// 第 4 天：休息。
// 第 5 天：完成任务 2 。
// 第 6 天：完成任务 3 。
// 第 7 天：休息。
// 第 8 天：完成任务 4 。
// 第 9 天：完成任务 5 。
// 可以证明无法少于 9 天完成所有任务。
// 示例 2：

// 输入：tasks = [5,8,8,5], space = 2
// 输出：6
// 解释：
// 6 天完成所有任务的一种方法是：
// 第 1 天：完成任务 0 。
// 第 2 天：完成任务 1 。
// 第 3 天：休息。
// 第 4 天：休息。
// 第 5 天：完成任务 2 。
// 第 6 天：完成任务 3 。
// 可以证明无法少于 6 天完成所有任务。
 

// 提示：

// 1 <= tasks.length <= 105
// 1 <= tasks[i] <= 109
// 1 <= space <= tasks.length

class Solution {
    public:
    long long taskSchedulerII(vector<int>& tasks, int space) {
        int n=tasks.size();
        long long ans=1;
        unordered_map<int, long long>last;
        last[tasks[0]]=1;
        for (int i=1;i<n;i++) {
            int x=tasks[i];
            if (last.find(x)!=last.end()&&last[x]+space>ans) {
                last[x]=ans=last[x]+space+1;
            }
            else {
                ans+=1;
                last[x]=ans;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,2,1,2,3,1};

    Solution so;
    cout << so.taskSchedulerII(arr,3) << endl;
    return 0;
}
