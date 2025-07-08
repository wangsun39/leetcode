#include "lc_pub.h"


class Solution {
    
    public:
    int maxEvents(vector<vector<int>>& events) {
        int n=events.size();
        int mn=100'001, mx=0;
        for (int i=0;i<n;i++) {
            mn=min(mn,events[i][0]);
            mx=max(mx,events[i][1]);
        }
        ranges::sort(events, [](const vector<int>& a, const vector<int>& b) {
                        if (a[0]==b[0]) return a[1] < b[1];
                        return a[0] < b[0];
                    });
        priority_queue<vector<int>, vector<vector<int>>,  decltype([](const vector<int>& a, const vector<int>& b) {
                        if (a[1]==b[1]) return a[0] > b[0];
                        return a[1] > b[1];
                    })> hp;

        int next=mn,ans=0;
        int j=0;
        for (int i=mn;i<=mx;i++) {
            while (j<n &&events[j][0]<=i) {
                hp.push(events[j]);
                j++;
            }
            while (hp.size()&&hp.top()[1]<i) hp.pop();
            if (hp.size()) {
                hp.pop();
                ans++;
            }
        }
        return ans;
    }
};
struct Compare {
    bool operator()(int a, int b) const {
        return a > b; // 返回 true 表示 b 的优先级更高
    }
};
int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[1,10],[1,2],[2,3],[2,2],[2,5]]");
    Solution so;
    cout<<so.maxEvents(arr)<<endl;

    std::priority_queue<int, std::vector<int>,less<int>> minHeap;

    // 插入元素
    minHeap.push(5);
    minHeap.push(2);
    minHeap.push(9);
    minHeap.push(1);
    minHeap.push(5);

    // 输出元素
    std::cout << "小顶堆的元素（从最小到最大）：" << std::endl;
    while (!minHeap.empty()) {
        std::cout << minHeap.top() << " "; // 访问优先级最高的元素（最小值）
        minHeap.pop(); // 移除优先级最高的元素
    }
    std::cout << std::endl;
    return 0;
}
