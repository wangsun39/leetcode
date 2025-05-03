#include "lc_pub.h"

using namespace std;

class Solution {
    public:
        string pushDominoes(string dominoes) {
            int n = dominoes.size();
            if (n==1) return dominoes;
            vector<int> left(n, n);  // 左侧最近的R的距离，初始化为n，表示最大值
            vector<int> right(n, n);  // 右侧最近的L的距离
            for (int i=1;i<n;i++) {
                if (dominoes[i]!='.') continue;
                if (dominoes[i-1]=='.') {
                    if (left[i-1]==n) left[i]=n;
                    else left[i]=left[i-1]+1;
                }
                else if (dominoes[i-1]=='L') left[i]=n;
                else left[i]=1;
            }
            for (int i=n-2;i>=0;i--) {
                if (dominoes[i]!='.') continue;
                if (dominoes[i+1]=='.') {
                    if (right[i+1]==n) right[i]=n;
                    else right[i]=right[i+1]+1;
                }
                else if (dominoes[i+1]=='R') right[i]=n;
                else right[i]=1;
            }
            string ans=dominoes;
            for (int i=0;i<n;i++) {
                if (ans[i]!='.'||left[i]==right[i]) continue;
                if (left[i]<right[i]) ans[i]='R';
                else ans[i]='L'; 
            }
            return ans;
        }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays = {1,1,2};
    Solution so;
    cout << so.pushDominoes("RR.L") <<endl;
    return 0;
}