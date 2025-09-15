#include "lc_pub.h"

class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        int bl[26] = {0};
        text += " ";
        for (auto c: brokenLetters) bl[c-'a'] = 1;
        bool flg = true;
        int ans=0;
        for (auto c: text) {
            if (c==' ') {
                if (flg) ans++;
                else flg=true;
            }
            else {
                if (bl[c-'a']) flg=false;
            }
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    auto v = so.canBeTypedWords("hello world", "ad");
    cout << v << endl;
    return 0;
}
