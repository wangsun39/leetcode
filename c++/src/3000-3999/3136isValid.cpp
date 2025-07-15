#include "lc_pub.h"


class Solution {
    public:
    bool isValid(string word) {
        if (word.size()<3) return false;
        int flg=0;
        for (auto x: word) {
            if (isalpha(x)) {
                char y=tolower(x);
                if (y=='a'||y=='e'||y=='i'||y=='o'||y=='u')flg|=1;
                else flg|=2;
            }
            else if(isdigit(x)) continue;
            else return false;
        }
        return flg==3;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> grid = parseGrid("[[5,7],[1,3],[9,10]]");

    Solution so;
    cout << so.isValid("234Adas") << endl;
    return 0;
}
