// https://www.algospot.com/judge/problem/read/PICNIC

#include <iostream>
#include <memory.h>
using namespace std;

int c, n, m;
int res = 0;
bool areFriends[10][10];
bool taken[10];

void count(){

    int firstFree = -1;
    for (int i=0; i<n; i++){
        if (!taken[i]){
            firstFree = i; // 짝 없는 첫번째 사람 찾기
            break;
        }
    }

    if (firstFree == -1){ // 만약 모두 짝이 있으면 res ++;
        res++;
        return;
    }

    for (int pair=firstFree+1; pair<n; pair++){ // 기본 DFS
        if(!taken[pair] && areFriends[firstFree][pair]){
            taken[firstFree] = taken[pair] = true;
            count();
            taken[firstFree] = taken[pair] = false;
        }
    }
}

int main(){

    cin >> c;
    while (c--){

        memset(areFriends,false, sizeof(areFriends)); // 배열 리셋
        memset(taken, false, sizeof(taken));
        cin >> n >> m;
        res = 0;

        for (int a, b, y=0; y<m; y++){ // 그래프 저장
            cin >> a >> b;
            areFriends[a][b] = areFriends[b][a] = true;
        }

        count();
        cout << res << "\n";
    }
}
