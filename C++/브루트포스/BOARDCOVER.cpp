// https://algospot.com/judge/problem/read/BOARDCOVER

#include <iostream>
#include <memory.h>
#include <string>
using namespace std;

int t, h, w, res;
int board[31][31];
int blockType[4][3][2] = {
	{{0,0},{1,0},{0,1}},
	{{0,0},{0,1},{1,1}},
	{{0,0},{1,0},{1,1}},
	{{0,0},{1,0},{1,-1}}
};

void DFS(){
    int x = -1, y = -1;
    for (int i=0; i<h; i++){
        for (int j=0; j<w; j++){
            if (board[i][j] == 0){
                x = i;
                y = j;
                break;
            }
        }
        if (x!=-1) break;
    }

    if (x==-1){
        res++;
        return;
    }

    for (int type=0; type<4; type++){
        bool check = true;
        for (int j=0; j<3; j++){
            int nx = x + blockType[type][j][0];
            int ny = y + blockType[type][j][1];
            if (nx < 0 || ny < 0 || nx >= h || ny >= w) {
				check = false;
				continue;
			}

            if ((board[nx][ny] += 1) > 1) check = false;
        }

        if (check == true) DFS();

        for (int j = 0; j < 3; j++) {
			int nx = x + blockType[type][j][0];
			int ny = y + blockType[type][j][1];
			if (nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
			board[nx][ny] -= 1;
		}
    }
}

int main()
{
    string tmp;
	cin >> t;
    
    while (t--){
        res = 0;
        int empty = 0;
        cin >> h >> w;

        for (int x=0; x<h; x++){
            
            cin >> tmp;
            for (int y=0; y<w; y++){
    
                if (tmp[y] == '#'){
                    board[x][y] = 1;
                } 
                else{
                    empty++;
                    board[x][y] = 0;
                }
                
            }
        }

        if (empty%3!=0){
            cout << "0\n";
            continue;
        }

        DFS();
        cout << res << "\n";
    }
}
