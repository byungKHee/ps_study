#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
using ll = long long;

int N, M, K;
ll Data[1000000];
vector<ll> tree;
ll Size = 1;

void update(int idx, ll val){
	int node = idx + Size;
	tree[node] = val;
	while(node > 1){
		node /= 2;
		tree[node] = tree[node*2] + tree[node*2+1];
	}
}

ll query(int left, int right){
	ll rnt = 0;
	left += Size;
	right += Size;
	while(left <= right){
		if(left % 2 == 1){
			rnt += tree[left];
			left ++;
		}
		left /= 2;
		if(right % 2 == 0){
			rnt += tree[right];
			right --;
		}
		right /= 2;
	}
	return rnt;
}

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> N >> M >> K;
	for(int i = 0; i < N; i++){
		cin >> Data[i];
	}
	while(Size < N){
		Size <<= 1;
	}
	tree.resize(2*Size, 0);
	for(int i = 0; i < N; i++){
		tree[i+Size] = Data[i];
	}
	for(int i = Size-1; i > 0; i--){
		tree[i] = tree[i*2] + tree[i*2+1];
	}
	for(int i = 0; i < M + K; i++){
		ll a,b,c; cin>>a>>b>>c;
		if(a==1){
			update(b-1, c);
		}
		else{
			cout << query(b-1,c-1) << "\n";
		}
	}
}