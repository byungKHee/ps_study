#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;
int N, M, T;
ll A[1002];
ll B[1002];
vector<ll> arr1;
vector<ll> arr2;

int main()
{
    A[0] = 0; B[0] = 0;
    cin >> T >> N;
    for(int i = 1; i < N+1; i++){
        int n; cin >> n;
        A[i] = A[i-1] + n;
    }
    cin >> M;
    for(int i = 1; i < M+1; i++){
        int n; cin >> n;
        B[i] = B[i-1] + n;
    }
    for(int i = 0; i < N; i++){
        for(int j = i+1; j < N+1; j++){
            arr1.push_back(A[j] - A[i]);
        }
    }
    for(int i = 0; i < M; i++){
        for(int j = i+1; j < M+1; j++){
            arr2.push_back(B[j] - B[i]);
        }
    }
    sort(arr1.begin(), arr1.end());
    sort(arr2.begin(), arr2.end());
    
    ll answer = 0;
    for(ll a : arr1){
        answer += upper_bound(arr2.begin(), arr2.end(), T-a) - lower_bound(arr2.begin(), arr2.end(), T-a);
    }
    cout << answer;

    return 0;
}