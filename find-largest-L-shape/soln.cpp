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

    int R = A.size();
    int C = A[0].size();

    // vector<vector<int>> B_row(R + 1);
    // for (int i = 0 ; i < R + 1 ; i++)
    //     B_row[i].resize(C + 1);

    // vector<vector<int>> B_col(R + 1);
    // for (int i = 0 ; i < R + 1 ; i++)
    //     B_col[i].resize(C + 1);

    // vector<vector<int>> B(R + 1);
    // for (int i = 0 ; i < R + 1 ; i++)
    //     B[i].resize(C + 1);

    int B_row [501][501] = {};
    int B_col [501][501] = {};
    int B [501][501] = {};

    int ct_len = 1 + ((min(R, C) >> 1) << 1);


    int pre = 0;
    for (int i = 0; i < R; ++i) {
        pre = 0;
        for (int j = C - 1; j >= 0; --j) {
            if (A[i][j] == 1) {
                if (pre == 1) {
                    B_row[i][j] = B_row[i][j + 1] + 1;
                } else {
                    B_row[i][j] = 1;
                }
            }
            pre = A[i][j];
        }
    }
    // for (int i=0;i<5;++i) {
    //     for (int j=0;j<5;++j) {
    //         cout<<B_row[i][j]<<" ";
    //     }
    //     cout<<endl;
    // } 
    for (int j = 0; j < C; ++j) {
        pre = 0;
        for (int i = 0; i < R; ++i) {
            if (A[i][j] == 1) {
                if (pre == 1) {
                    if (i - 1 >= 0) {
                        B_col[i][j] = B_col[i - 1][j] + 1;
                    } else {
                        B_col[i][j] = 1;
                    }
                } else {
                    B_col[i][j] = 1;
                }
            }
            pre = A[i][j];
        }
    }
    // for (int i=0;i<5;++i) {
    //     for (int j=0;j<5;++j) {
    //         cout<<B_col[i][j]<<" ";
    //     }
    //     cout<<endl;
    // } 
    // take min
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            B[i][j] = min(B_row[i][j],B_col[i][j]);
        }
    }


    // for (int i=0;i<5;++i) {
    //     for (int j=0;j<5;++j) {
    //         cout<<B[i][j]<<" ";
    //     }
    //     cout<<endl;
    // } 

    int ct [501]; // vector<int> ct(1 + ((min(R, C) >> 1) << 1)); // vector<int> ct(1 + min(R, C) / 2 * 2);

    // cout<<"min"<<min(R, C)<<endl<<endl;
    // for (int ttmp=0; ttmp<ct.size();++ttmp) cout<<ct[ttmp]<<", ";cout<<endl;

    int ans = 0;

    // [1 ~ R-1][0]
    for (int s = 1; s < R; ++s) {
        // cout<<"="<<endl;
        for (int t = 0; s - t >= 0 && t < C; ++t) {
            // cout<<s-t<<t<<endl;
            for (int l = 2; l < ct_len; l += 2) {
                if (B[s-t][t] >= l - ct[l]) {
                    ++ct[l];
                } else {
                    ct[l] = 0;
                }
                if (l >> 1 == ct[l]) {
                    ans = max(ans, l);
                    // cout<<"cand"<<l/2<<endl;
                }
                // for (int ttmp=0; ttmp<ct.size();++ttmp) cout<<ct[ttmp]<<", ";cout<<endl;
            }
        }
        // reset C
        for (int l = 2; l < ct_len; l += 2) {
            ct[l] = 0;
        }
    }
    // [R-1][1 ~ C-2]
    for (int s = 1; s < C - 1; ++s) {
        // cout<<"="<<endl;
        for (int t = 0; R - 1 - t >= 0 && s + t < C; ++t) {
            // cout<<R - 1 - t<<t+s<<endl;
            for (int l = 2; l < ct_len; l += 2) {
                if (B[R - 1 - t][s + t] >= l - ct[l]) {
                    ++ct[l];
                } else {
                    ct[l] = 0;
                }
                if (l >> 1 == ct[l]) {
                    ans = max(ans, l);
                    // cout<<"cand"<<l/2<<endl;
                }
                // for (int ttmp=0; ttmp<ct.size();++ttmp) cout<<ct[ttmp]<<", ";cout<<endl;
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

    // std::vector<int> v(5);
    // for (int i=0; i<v.size();++i) cout<<v[i]<<endl;

}

