#include "lc_pub.h"

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int n=s.size();
        int left[26]={-1},right[26]={-1};
        memset(left,-1,sizeof(left));
        memset(right,-1,sizeof(right));
        for (int i=0;i<n;i++) {
            if (left[s[i]-'a']==-1) left[s[i]-'a']=i;
        }
        for (int i=n-1;i>=0;i--) {
            if (right[s[i]-'a']==-1) right[s[i]-'a']=i;
        }
        int ans=0;
        for (char i='a';i<='z';i++) {
            int vis[26]={0};
            for (int j=left[i-'a']+1;j<right[i-'a'];j++) {
                vis[s[j]-'a']=1;
            }
            for (int x: vis) ans+=x;
        }
        return ans;
    }

};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,3};
    // vector<vector<int>> grid = parseGrid("[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]");
    // cout << grid.size() << "  " << grid[0].size()<< endl;

    Solution so;
    auto v = so.countPalindromicSubsequence("uuu");
    cout << v << endl;
    return 0;
}
