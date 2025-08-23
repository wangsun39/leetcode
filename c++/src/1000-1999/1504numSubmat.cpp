#include "lc_pub.h"


class Solution {
    
    public:
    int numSubmat(vector<vector<int>>& mat) {
        int r=mat.size(),c=mat[0].size();
        vector up(r, vector<int>(c,0));  // 每个点上方有多少个连续的1
        up[0] = mat[0];
        for (int i=1;i<r;i++) {
            for (int j=0;j<c;j++) {
                if (mat[i][j])
                    up[i][j]=up[i-1][j]+1;
            }
        }
        int ans=0;
        for (int i=0;i<r;i++) {
            stack<int> st;
            vector<int> dp(c, 0);  // 在i行以[i,j]为右下角的矩形个数
            for (int j=0;j<c;j++) {
                while(st.size()&&up[i][st.top()]>=up[i][j]) {
                    st.pop();
                }
                if (up[i][j]) {
                    if (st.size())
                        dp[j]=dp[st.top()]+up[i][j]*(j-st.top());
                    else
                        dp[j]=up[i][j]*(j+1);
                    ans+=dp[j];
                }
                else
                    dp[j]=0;
                st.push(j);
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    auto arr=parseGrid("[[1,0,1],[1,1,0],[1,1,0]]");
    auto v = so.numSubmat(arr);
    cout << v << endl;
    return 0;
}
