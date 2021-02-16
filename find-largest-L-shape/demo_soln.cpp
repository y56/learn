#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

void myprint(vector<vector<int>> B) {
    for (int i=0;i<B.size();++i) {
        for (int j=0;j<B[i].size();++j) {
            cout<<B[i][j]<<" ";
        }
        cout<<endl;
    }
}

int soln(vector<vector<int>> A) {

    int R = A.size(); // num of row
    int C = A[0].size(); // num of col

    // matrix A, max to 500*500

    // 0 0 0 1 1 1 1 1 0 1 1 0 0 1 1 1 // A[][]
    // 0 0 0 5 4 3 2 1 0 2 1 0 0 3 2 1 // B_row[][]
    
    // 500 is enough
    int B_row [501][501] = {}; // B_row[i][j] = A[i][j] +~ A[i][k] // where continuous 1 for j~k  
    int B_col [501][501] = {}; // by default initiate as 0s
    int B [501][501] = {}; // B[i][j] is the max of B_row[i][j] and B_col[i][j]

    int ct_len = 1 + ((min(R, C) >> 1) << 1); 
    // ((min(R, C) >> 1) << 1) is the possible max ans // +1 just for for-loop bound check

    int pre = 0; // previous
    for (int i = 0; i < R; ++i) {
        pre = 0; // reset for each row // take care of boundary issue
        for (int j = C - 1; j >= 0; --j) { // right to left
            if (A[i][j] == 1) { 
                if (pre == 1) { // 1 here and 1 before // accumulate it
                    B_row[i][j] = B_row[i][j + 1] + 1;
                } else {
                    B_row[i][j] = 1; // a new star of a continuous row
                }
            }
            pre = A[i][j]; // update pre
        }
    }

    for (int j = 0; j < C; ++j) {
        pre = 0;
        for (int i = 0; i < R; ++i) { // up to down
            if (A[i][j] == 1) {
                if (pre == 1) { 
                    // useless judgment !
                    if (i - 1 >= 0) { // i>=1
                        B_col[i][j] = B_col[i - 1][j] + 1;
                    } else { // i==0
                        B_col[i][j] = 1;
                    }
                } else {
                    B_col[i][j] = 1;
                }
            }
            pre = A[i][j];
        }
    }

    // take min
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            B[i][j] = min(B_row[i][j],B_col[i][j]);
        }
    }

    int ct [501]; // only use even 2,4,6...th element // 500 is enough

    int ans = 0;

    // [1 ~ R-1][0] // scan diagonal from top to bottom // within diagonal, from bottom to top 
    for (int s = 1; s < R; ++s) {
        for (int t = 0; s - t >= 0 && t < C; ++t) {
            for (int l = 2; l < ct_len; l += 2) { // l:=side length of fat L-shape 
            // start from 2 // step by 2// don't exceed ((min(R, C) >> 1) << 1)
                if (B[s-t][t] >= l - ct[l]) { // for fat L-shape with sidelen l, we need slim L's of 2l*2l~l*l
                 
                    ++ct[l];
                } else {
                    ct[l] = 0;
                }
                if (l >> 1 == ct[l]) {
                    ans = max(ans, l);
                }
            }
        }
        // reset C
        for (int l = 2; l < ct_len; l += 2) {
            ct[l] = 0;
        }
    }
    // [R-1][1 ~ C-2]
    for (int s = 1; s < C - 1; ++s) {
        for (int t = 0; R - 1 - t >= 0 && s + t < C; ++t) {
            for (int l = 2; l < ct_len; l += 2) {
                if (B[R - 1 - t][s + t] >= l - ct[l]) {
                    ++ct[l];
                } else {
                    ct[l] = 0;
                }
                if (l >> 1 == ct[l]) {
                    ans = max(ans, l);
                }
            }
        }
        // reset C
        for (int l = 2; l < ct_len; l += 2) {
            ct[l] = 0;
        }
    }
    return ans / 2;
}

int main() {
    //Solution s;
    vector<vector<int>> A {{1,1,1,1,1,1},
                           {1,1,1,1,1,1},
                           {1,1,1,1,1,1},
                           {1,1,1,1,1,1},
                           {1,1,1,1,1,1}}; 
    
    myprint(A);

    int tmp = soln(A);
    cout<<"ans"<<tmp<<endl;
}

