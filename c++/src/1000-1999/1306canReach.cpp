#include "lc_pub.h"


class Solution {
    public:
    bool canReach(vector<int>& arr, int start) {
        int n=arr.size();
        vector<int> vis(n, 0);
        auto dfs = [&](this auto&& dfs, int i) -> bool {
            if (arr[i]==0) return true;
            int j=i-arr[i];
            vis[i]=1;
            if (j>=0&&j<n&&!vis[j]) {
                if(dfs(j)) return true;
            }
            j=i+arr[i];
            if (j>=0&&j<n&&!vis[j]) {
                if(dfs(j)) return true;
            }
            return false;
        };
        return dfs(start);
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    vector<int>arr{4,2,3,0,3,1,2};
    cout<<so.canReach(arr,0)<<endl;
    return 0;
}
