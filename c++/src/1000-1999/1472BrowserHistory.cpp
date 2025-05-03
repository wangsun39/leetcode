#include "lc_pub.h"

class BrowserHistory {
public:
    BrowserHistory(string homepage) {
        vs.emplace_back(homepage);
        cur = 0;
    }
    
    void visit(string url) {
        // vs.erase(vs.begin() + cur + 1, vs.end());  两种写法都可以
        vs.resize(cur + 1);
        vs.emplace_back(url);
        cur ++;
    }
    
    string back(int steps) {
        cout<<cur<<endl;
        cur -= steps;
        if (cur < 0) cur = 0;
        return vs[cur];
    }
    
    string forward(int steps) {
        cur += steps;
        if (cur >= vs.size()) cur = vs.size() - 1;
        return vs[cur];
    }
    vector<string> vs;
    int cur;
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    BrowserHistory so("leetcode.com");
    so.visit("google.com");
    cout << so.back(1) << endl;
    return 0;
}
