#include "lc_pub.h"


class Solution {
    public:
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        stack<int> st;
        for (auto x: nums) {
            if (st.size() == 0) 
            {
                st.push(x);
                continue;
            }
            int y = st.top();
            while (st.size() && gcd(x, y) > 1) {
                st.pop();
                x = lcm(x, y);
                if (st.size()) y = st.top();
            }
            st.push(x);
        }
        vector<int>ans(st.size());
        for (int i=st.size()-1;i>=0;i--) {
            ans[i]=st.top();
            st.pop();
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
