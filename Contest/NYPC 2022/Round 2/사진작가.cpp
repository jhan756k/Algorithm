#include <iostream>
using namespace std;

int n, startcount=0;
int nlist[1000001];
int dp[200001];
int maxn = -1;

int main(){
    cin >> n;
    for (int x=0; x<n; x++){
        cin >> nlist[x];
    }

    dp[0] = 1;

    for (int x=1; x<n; x++){
        dp[x] = dp[x-1]+1;
        for (int p=x-1; p>=startcount; p--){
            if (nlist[x] == nlist[p]){
                startcount = p+1;
                dp[x] = x-p;
                break;
            }
        }

        if (dp[x] > maxn){
            maxn = dp[x];
        }
    }

    cout << maxn;
}
