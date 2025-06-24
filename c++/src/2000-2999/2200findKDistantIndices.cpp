#include "lc_pub.h"


class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        vector<int> ans;
        int n=nums.size();
        for (int i=0;i<n;i++) {
            if (nums[i]==key) {
                int start=max(0,i-k);
                if (ans.size()!=0&&ans[ans.size()-1]+1>start) start=ans[ans.size()-1]+1;
                for (int j=start;j<=min(i+k,n-1);j++) {
                    ans.emplace_back(j);
                }
            }
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr = parseGrid("[[3,2],[4,3],[4,4],[2,5]]");
    vector<int> n1{3,4,9,1,3,9,5}, n2{0,1,2,3};

    Solution so;
    cout << so.findKDistantIndices(n1, 9,1) << endl;
    return 0;
}
