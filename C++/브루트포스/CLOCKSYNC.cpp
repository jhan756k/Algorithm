#include <iostream>
#include <algorithm>
using namespace std;

const int INF = 99999;
int t;
int clocks[16];
int button[10][16] = {
    {1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0},
	{0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1},
	{1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0},
	{1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1},
	{0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1},
	{0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1},
	{0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0}
};

bool check(){
    for (int x=0; x<16; x++){
        if (clocks[x] != 12) return false;
    }
    return true;
}

void switch_clock(int bn){
    for (int x=0; x<16; x++){
        if (button[bn][x] == 1){
            clocks[x] += 3;
            if (clocks[x] == 15) clocks[x] = 3;
        }
    }
}

int solve(int switch_n){
    if (switch_n == 10){ // 모든 버튼 다 고려했으면 
        if (check()) return 0; // 만약 모두 12 이면 그냥 리턴
        else return INF; // 안되면 무한대 반환
    }

    int ret = INF;
    for (int i=0; i<4; i++){ // 4번까지 순회하면 원래대로 돌아옴
        ret = min(ret, i + solve(switch_n+1));
        switch_clock(switch_n);
    }

    return ret;
}

int main(){
    cin >> t;

    while (t--){
        for (int x=0; x<16; x++) cin >> clocks[x];

        int result = solve(0);
        if (result == INF) cout << -1 << "\n";
        else cout << result << "\n";
    }
}
