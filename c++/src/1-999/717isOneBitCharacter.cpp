#include "lc_pub.h"

using namespace std;

class Solution {
public:
    bool judgePoint24(vector<int>& cards) {
        ranges::sort(cards);  // 用 next_permutation 必须先排序
        auto calc = [](double x, char op, double y) -> double {
            switch (op) {
                case '+': return x + y;
                case '-': return x - y;
                case '*': return x * y;
                default: return y == 0 ? 100000000 : (double)x / y;
            }
        };
        char ops[]={'+','-','*','/'};
        do {
            int a=cards[0],b=cards[1],c=cards[2],d=cards[3];
            for (char op1: ops)
                for (char op2: ops)
                    for (char op3: ops) {
                        if (abs(calc(calc(a,op1,b),op2,calc(c,op3,d)) - 24)<0.0000001) 
                        return true;
                        if (abs(calc(calc(calc(a, op1, b), op2, c), op3, d) - 24) < 0.0000001) 
                        return true;
                        if (abs(calc(a, op1, calc(b, op2, calc(c, op3, d))) - 24) < 0.0000001) 
                        return true;
                        if (abs(calc(a, op1, calc(calc(b, op2, c), op3, d)) - 24) < 0.0000001) 
                        return true;
                        if (abs(calc(calc(a, op1, calc(b, op2, c)), op3, d) - 24) < 0.0000001) 
                        return true;
                    }
            
        } while (std::next_permutation(cards.begin(), cards.end()));
        return false;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays{8,1,6,6};
    Solution so;
    cout << so.judgePoint24(arrays) <<endl;
    return 0;
}