#include "lc_pub.h"

class Bank {
    vector<long long> mb;
    int n;
public:
    Bank(vector<long long>& balance) {
        mb = balance;
        n = mb.size();
    }
    
    bool transfer(int account1, int account2, long long money) {
        if (account1>0&&account1<=n&&account2>0&&account2<=n&&mb[account1-1]>=money) {
            mb[account1-1]-=money;
            mb[account2-1]+=money;
            return true;
        }
        return false;
    }
    
    bool deposit(int account, long long money) {
        if (account>0&&account<=n) {
            mb[account-1]+=money;
            return true;
        }
        return false;
    }
    
    bool withdraw(int account, long long money) {
        if (account>0&&account<=n&&mb[account-1]>=money) {
            mb[account-1]-=money;
            return true;
        }
        return false;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {7,1,5,4};

    return 0;
}
