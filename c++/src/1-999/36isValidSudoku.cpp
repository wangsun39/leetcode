#include "lc_pub.h"


class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i=0;i<9;i++) {
            int counter[9]={0};
            for (int j=0;j<9;j++) 
                if (board[i][j]!='.') {
                    counter[board[i][j]-'1']++;
                    if (counter[board[i][j]-'1']>1) return false;
                }
        }
        for (int i=0;i<9;i++) {
            int counter[9]={0};
            for (int j=0;j<9;j++) 
                if (board[j][i]!='.') {
                    counter[board[j][i]-'1']++;
                    if (counter[board[j][i]-'1']>1) return false;
                }
        }
        for (int i=0;i<9;i+=3) {
            for (int j=0;j<9;j+=3) {
                int counter[9]={0};
                for (int k=0;k<3;k++) {
                    for (int t=0;t<3;t++)
                        if (board[i+k][j+t]!='.') {
                            counter[board[i+k][j+t]-'1']++;
                            if (counter[board[i+k][j+t]-'1']>1) return false;
                        }
                }
            }
        }
        return true;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<std::vector<int>> obstacleGrid = {
        {0, 0, 0},
        {0, 1, 0},
        {0, 0, 0}
    };
    Solution so;
    // cout << so.isValidSudoku(obstacleGrid) <<endl;
    return 0;
}