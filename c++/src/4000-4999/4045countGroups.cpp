// 给你一个 严格递增 的整数数组 position，其中 position[i] 是第 i 个机器人（下标从 0 开始）在时间 t = 0 时的初始位置。

// 另给你一个整数数组 speed，其中 speed[i] 是第 i 个机器人的恒定速度（单位：单位/秒），以及一个整数 distance。

// 时间是连续的，以秒为单位。速度为 v 的机器人或机器人组在任意 t 秒的时间间隔内向右移动 v * t 个单位。

// 每当两个机器人或组之间的距离至多为 distance 时，它们就会合并成一个机器人组。

// 如果多个机器人或机器人组在同一时间满足合并条件，则所有合并 同时 发生。具体而言，任何相邻位置相差至多为 distance 的相连机器人或组都会合并为一个机器人组。

// 合并后，生成的机器人组将继承该组中 最右侧机器人 的当前位置和速度。一旦合并，机器人将永不分离。

// 返回在所有可能的合并发生后剩余的组数。

// 如果数组中的每个元素都严格大于其前一个元素（如果存在），则该数组是 严格递增 的。

 

// 示例 1：

// 输入： position = [1,5,6,20], speed = [4,3,2,3], distance = 1

// 输出： 2

// 解释：



// 最初，组为 {R1}、{R2}、{R3} 和 {R4}。
// 在 t = 0 时，分别位于位置 5 和 6 的机器人 R2 和 R3 合并，因为它们相距 1 个单位。生成的组以最右侧机器人 R3 的位置和速度移动。现在的组为 {R1}、{R2, R3} 和 {R​4}。
// 随后在 t = 2 时，机器人 R1 追上组 {R2, R3} 并与其合并。现在的组为 {R1, R2, R3} 和 {R​4}。
// 因此，答案是 2。

// 示例 2：

// 输入： position = [1,5,9], speed = [3,2,2], distance = 2

// 输出： 2

// 解释：



// 最初，组为 {R1}、{R2} 和 {R3}。
// 在 t = 2 时，机器人 R1 追上机器人 R2 并与其合并。生成的组以最右侧机器人 R2 的位置和速度移动。现在的组为 {R1, R2} 和 {R3}。
// 因此，答案是 2。

// 示例 3：

// 输入： position = [9], speed = [8], distance = 5

// 输出： 1

// 解释：

// 最初只有一个组。因此，答案是 1。

 

// 提示：

// 1 <= position.length == speed.length <= 105
// 1 <= position[i], speed[i], distance <= 109
// position 严格递增。

#include "lc_pub.h"

class Solution {
public:
    int countGroups(vector<int>& position, vector<int>& speed, int distance) {
        int n=position.size();
        vector<int> p, s;
        p.push_back(position[0]);
        s.push_back(speed[0]);
        for (int i=1;i<n;i++) {
            int m=p.size();
            if (position[i]-p[m-1]<=distance) {
                p[m-1]=position[i];
                s[m-1]=speed[i];
            }
            else {
                p.push_back(position[i]);
                s.push_back(speed[i]);
            }
        }

        n=p.size();
        int ans=1;
        for (int i=n-2;i>=0;i--) {
            if (s[i]<=s[i+1])
                ans++;
            else {
                s[i]=s[i+1];
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{499,499,499};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
