#include <iostream>
#include <queue>
#include <cstring>
using namespace std;
 
int board[301][301];
bool vis[301][301];
 
int dx[8] = {1,2,2,1,-1,-2,-2,-1};
int dy[8] = {2,1,-1,-2,-2,-1,1,2};
 
int I;
queue<pair<int, int>> dQ;
int sx, sy, ex, ey;
 
void BFS(int a, int b){
    dQ.push(make_pair(a, b));
    vis[a][b] = true;

    while(!dQ.empty()){
        int x = dQ.front().first;
        int y = dQ.front().second;
        dQ.pop();
        
        if(x == ex && y == ey){
            cout << board[x][y] << '\n';
            
            while(!dQ.empty()){
                dQ.pop();
            }
            break;
        }
        
        for(int i = 0; i < 8; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx >= 0 && nx < I && ny >= 0 && ny < I){
                if(vis[nx][ny] == false){
                    vis[nx][ny] = true;
                    board[nx][ny] = board[x][y] + 1;
                    dQ.push(make_pair(nx, ny));
                }
            }
        }
    }
}
 
int main() {
    int t;
    cin >> t;
 
   while (t--){
        cin >> I;
        cin >> sx >> sy >> ex >> ey;
        BFS(sx, sy);
        memset(board, 0, sizeof(board));
        memset(vis, false, sizeof(vis));
    }
    return 0;
}
