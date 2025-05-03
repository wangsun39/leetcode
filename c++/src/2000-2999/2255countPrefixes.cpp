#include "lc_pub.h"

class RangeFreqQuery {
public:
int countPrefixes(vector<string>& words, string s) {
    return ranges::count_if(words, [&](string x)->bool{
        return s.starts_with(x);
    });
}
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> arr = {"a","b","c","ab","bc","abc"};

    RangeFreqQuery so;
    cout << so.countPrefixes(arr, "abc") << endl;
    return 0;
}
