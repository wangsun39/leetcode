#include "lc_pub.h"

class Solution {
    public:
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        int n=fruits.size();
        int ans=0;
        int s=0,l,r;
        int p1=-1,p2=n;
        for (int i=0;i<n;i++) {
            if (fruits[i][0]>startPos) break;
            p1=i;
        }
        for (int i=n-1;i>=0;i--) {
            if (fruits[i][0]<startPos) break;
            p2=i;
        }
        if (p1>=0) {
            r=p2-1;
            int sr=max(p2,p1+1);
            for (int i=sr;i<n;i++) { // 计算向右最多能走多少
                if (fruits[i][0]-startPos>k) break;
                s+=fruits[i][1];
                r=i;
            }
            ans=max(ans,s);
            // 先向左走
            for (int i=p1;i>=0;i--) {
                if (startPos-fruits[i][0]>k) break;
                s+=fruits[i][1];
                while (r>=sr&&(startPos-fruits[i][0])*2+fruits[r][0]-startPos>k) {
                    s-=fruits[r][1];
                    r--;
                }
                ans=max(ans,s);
               }
        }
        s=0;
        if (p2<n) {
            l=p1+1;
            int sl=min(p1,p2-1);
            for (int i=sl;i>=0;i--) { // 计算向左最多能走多少
                if (startPos-fruits[i][0]>k) break;
                s+=fruits[i][1];
                l=i;
            }
            ans=max(ans,s);
            // 先向右走
            for (int i=p2;i<n;i++) {
                if (fruits[i][0]-startPos>k) break;
                s+=fruits[i][1];
                while (l<=sl&&(fruits[i][0]-startPos)*2+startPos-fruits[l][0]>k) {
                    s-=fruits[l][1];
                    l++;
                }
                ans=max(ans,s);
               }
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> fruits = parseGrid("[[2,8],[6,3],[8,6]]");

    Solution so;
    cout << so.maxTotalFruits(fruits,5,4) << endl;
    return 0;
}
