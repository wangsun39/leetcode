#include "lc_pub.h"


class Solution {
    public:
    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        auto check1 = [](string x) -> bool {
            if (x.size()==0) return false;
            for (auto y: x) {
                if ('a'<=y&&y<='z') continue;
                if ('A'<=y&&y<='Z') continue;
                if ('0'<=y&&y<='9') continue;
                if (y=='_') continue;
                return false;
            }
            return true;
        };
        auto check2 = [](string x) -> bool {
            if (x=="electronics"||x=="grocery"||x=="pharmacy"||x=="restaurant") return true;
            return false;
        };
        vector<pair<string, string>> vp;
        int n=code.size();
        for (int i=0;i<n;i++) {
            if (check1(code[i])&&check2(businessLine[i])&&isActive[i]) 
                vp.push_back({businessLine[i], code[i]});
        }
        ranges::sort(vp);
        vector<string> ans;
        for (auto &[a, b]: vp) {
            ans.push_back(b);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>>connections= parseGrid("[[1,2],[2,3],[3,4],[4,5]]");
    vector<vector<int>>q= parseGrid("[[1,3],[2,1],[1,1],[2,2],[1,2]]");

    Solution so;
    return 0;
}
