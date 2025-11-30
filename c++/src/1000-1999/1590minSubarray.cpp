#include "lc_pub.h"

class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int n=nums.size();
        unordered_map<int, int> id_map;
        int ans=n;
        int s=0,t=0;
        id_map[0]=-1;
        for (int i=0;i<n;i++) {
            t+=nums[i];
            t%=p;
        }
        // 目标是移除区间和模p为t的子区间
        if (t==0) return 0;
        for (int i=0;i<n;i++) {
            s+=nums[i];
            s%=p;
            int t1=(s+p-t)%p;
            if (id_map.find(t1)!=id_map.end()) {
                if (i - id_map[t1] < ans) {
                    ans = i - id_map[t1];
                }
            }
            id_map[s] = i;
        }
        if (ans==n) return -1;
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> p = {1,2,3,4,7};
    Solution so;
    return 0;
}
