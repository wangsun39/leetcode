

#include "lc_pub.h"

int seats[100000][4];

class BusBooking {
public:
    BusBooking(int n) {
        memset(&seats, 0, n * sizeof(int) * 4);
        total=a=d=bc=0;
    }
    
    void toggle(string seat) {
        int r=stoi(seat.substr(1))-1;
        int c=seat[0]-'A';
        if (c==1||c==2) {
            if (seats[r][c])
            {
                bc--;
                total--;
            }
            else {
                bc++;
                total++;
            }
            seats[r][c]^=1;
        }
        else if (c==0) {
            if (seats[r][c]) {
                total-=seats[r][c];
                seats[r][c]=0;
                a--;
            }
            else {
                if (seats[r][c+1]) {
                    total+=3;
                    seats[r][c]=3;
                }
                else {
                    total++;
                    seats[r][c]=1;
                }
                a++;
            }
        }
        else {
            if (seats[r][c]) {
                total-=seats[r][c];
                seats[r][c]=0;
                d--;
            }
            else {
                if (seats[r][c-1]) {
                    total+=3;
                    seats[r][c]=3;
                }
                else {
                    total++;
                    seats[r][c]=1;
                }
                d++;
            }
        }
    }
    
    int getTotalTime() {
        return total;
    }
    
    int getMinTime() {
        return a+bc+d;
    }
private:
    int total;
    int a;
    int bc;
    int d;
};

/**
 * Your BusBooking object will be instantiated and called as such:
 * BusBooking* obj = new BusBooking(n);
 * obj->toggle(seat);
 * int param_2 = obj->getTotalTime();
 * int param_3 = obj->getMinTime();
 */

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{-58,4,24,23};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
