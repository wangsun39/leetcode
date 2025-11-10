#include "lc_pub.h"


class Solution {
    public:
    int minOperations(vector<int>& nums) {
        int ans=0;
        stack<int> st;
        for (int x: nums) {
            while (st.size() && st.top() > x) {
                st.pop();
            }
            if ((st.size() && st.top() == x) || x == 0) continue;
            st.push(x);
            ans++;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{7,2,0,4,2};

    Solution so;
    cout<<so.minOperations(nums)<<endl;
    return 0;
}
