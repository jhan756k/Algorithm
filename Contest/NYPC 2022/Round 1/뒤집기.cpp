#include <iostream>
#include<algorithm>
using namespace std;

int main(){
	int n;
	int nlist[n+2];
	int dp[n+2];
	int resm, tmp, tp;
	cin >> n;
	
	for (int x=0; x<n; x++){
		cin >> nlist[x];
	}
		
	if (n==1){
		cout << nlist[0];
		return 0;
	}
	
	for (int l=0; l<n; l++){
		for (int r=l+1; r<n; r++){
			
			tmp = (r-l+1)/2;
			
			for (int x=0; x<tmp; x++){
				tp = nlist[l+x];
				nlist[l+x] = nlist[r-x];
				nlist[r-x] = tp;
			}
			
			dp[0] = nlist[0];
			
			
			for (int y=1; y<n; y++){
				dp[y] = max(dp[y-1]+nlist[y], nlist[y]);
				if (dp[y] > resm){
					resm = dp[y];
				}
			}
			
			for (int a=0; a<tmp; a++){
				tp = nlist[l+a];
				nlist[l+a] = nlist[r-a];
				nlist[r-a] = tp;
			}
			
		}
	}
	
	cout << resm;	
}

