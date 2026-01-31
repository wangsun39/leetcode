#include "lc_pub.h"

using namespace std;

class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        auto p = ranges::upper_bound(letters, target);
        if (p == letters.end()) return letters[0];
        return *p;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays{8,1,6,6};
    Solution so;
    return 0;
}