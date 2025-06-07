#include "lc_pub.h"

class Solution {
    public:
    string robotWithString(string s) {
        int n = s.size();
        string ans(n, ' ');
        int idx = 0;
        unordered_map<char, int> after;  // after[x] 表示 比 x 小的字符的最大下标
        for (char c='a';c<'z';c++) {
            after[c]=-1;
        }
        stack<int> st;
        char p = 'z';
        for (int i=n-1;i>=0;i--) {
            for (char j=s[i]+1;j<=p;j++) {
                after[j] = i;
            }
            p=min(p, s[i]);
        }
        for (int i=0;i<n;i++) {
            char x = s[i];
            if (!st.size()||st.top() >= x) {
                st.push(x);
                continue;
            }

            while (st.size() && after[st.top()] < i) {
                char y = st.top();
                st.pop();
                ans[idx++]=y;
            }
            st.push(x);
        }
        while (st.size()) {
            char y = st.top();
            st.pop();
            ans[idx++]=y;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {4,1,3,3};

    Solution so;
    cout << so.robotWithString("bdda") << endl;
    return 0;
}
