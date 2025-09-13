#include "lc_pub.h"


class Solution {
    public:
    int maxFreqSum(string s) {
        unordered_map<char,int> counter;
        int c1=0,c2=0;
        for (char c: s) {
            counter[c]++;
            if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u') c1=max(c1,counter[c]);
            else c2=max(c2, counter[c]);
        }
        return c1+c2;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    cout<<so.maxFreqSum("successes")<<endl;
    return 0;
}
