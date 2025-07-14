#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define TOTAL 1000001
int N;
int Size = 1;
vector<int> tree;


void update(int idx, int diff){
	int node = idx + Size;
	tree[node] += diff;
	while(node > 1){
		node /= 2;
		tree[node] += diff;
	}
}

int query(int node, int nodeL, int nodeR, int val){
	if(Size <= node){
		return node - Size + 1;
	}
	int mid = (nodeL + nodeR) / 2;
	int left = tree[node*2];
	if(left >= val){
		return query(node*2, nodeL, mid, val);
	}
	else{
		return query(node*2+1, mid+1, nodeR, val - left);
	}
}

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	while(Size < TOTAL) Size <<= 1;
	tree.resize(Size*2, 0);
	cin >> N;
	for(int i = 0; i < N; i++){
		int a; cin >> a;
		if(a == 2){
			int b,c; cin >> b >> c;
			update(b-1,c);
		}
		else{
			int b; cin >> b;
			int rnt = query(1, 0, TOTAL-1, b);
			cout << rnt << "\n";
			update(rnt-1, -1);
		}
	}
}