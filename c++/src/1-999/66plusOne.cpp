#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry=0;
        int n=digits.size();
        digits[n-1]++;
        for (int i=n-1;i>=0;i--) {
            digits[i]+=carry;
            if (digits[i]>9) {
                digits[i]=0;
                carry=1;
            }
            else {
                carry=0;
            }
        }
        if (carry) digits.insert(digits.begin(), 1);
        return digits;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}