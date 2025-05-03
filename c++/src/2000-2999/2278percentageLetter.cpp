#include "lc_pub.h"

class Solution {
    public:
    int percentageLetter(string s, char letter) {
        int in=0;
        for (auto x: s) {
            if (x==letter) in++;
        }
        return in*100/s.size();
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    auto v = so.percentageLetter("foobar",'o');
    // auto v = so.countOfSubstrings("aeiou",0);
    cout << v << endl;
    return 0;
}
