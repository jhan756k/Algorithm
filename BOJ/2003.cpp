#include <iostream>
using namespace std;

int n, m, partsum=0, sp=0, ep=0, res=0;
int nlist[10001];

int main(){
    cin >> n >> m;

    for (int i=0; i<n; i++){
        cin >> nlist[i];
    }

    while (ep<=n){
        if (partsum >= m){
            partsum -= nlist[sp++];
        } else if (partsum < m){
            partsum += nlist[ep++];
        }

        if (partsum == m){
            res++;
        }
    }

    cout << res;
    return 0;
}
