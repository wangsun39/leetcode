#include "lc_pub.h"

class Solution {
    
    public:
    string fractionToDecimal(int numerator, int denominator) {
        string ans;
        if ((long long)numerator * denominator < 0) ans="-";
        long long n1 = numerator,n2=denominator;
        n1=abs(n1);
        n2=abs(n2);
        vector<long long> res;
        long long a=(n1%n2)*10,b=n2;
        long long q,r=0;
        q=n1/n2;
        ans += to_string(q) + ".";
        unordered_map<long long, int> pos;
        int i = 0,start=-1;
        while(a) 
        {
            q=a/b;
            r=a%b;
            res.push_back(q);
            pos[a] = i;
            if (r==0) break;
            if (pos.find(r*10)!=pos.end()) {
                start = pos[r*10];
                break;
            }

            i++;
            a=r*10;
        }
        if (start==-1) start=res.size();
        for (int i=0;i<start;i++) {
            ans.append(to_string(res[i]));
        }
        if (r) {
            ans.append("(");
            for (int i=start;i<res.size();i++) {
                ans.append(to_string(res[i]));
            }
            ans.append(")");
        }
        if (ans.back() == '.') ans.erase(ans.size() - 1);
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int>ratings{1,3,4,5,2};

    Solution so;
    auto v = so.fractionToDecimal(4,333);
    cout << v << "," << so.fractionToDecimal(1,6) << "," << so.fractionToDecimal(-50,8) << endl;
    return 0;
}
