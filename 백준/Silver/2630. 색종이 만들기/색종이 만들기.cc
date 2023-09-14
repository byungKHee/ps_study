#include <cstdio>
int N, arr[128][128];
int white = 0;
int blue = 0;
void func(int x, int y, int n){
    bool check = true;
    for(int i = x; i < x + n; i++){
        for(int j = y; j < y + n; j++){
            if(arr[x][y] != arr[i][j]){
                check = false;
                break;
            }
        }
    }
    if(check && arr[x][y] == 0)
        white++;
    else if(check && arr[x][y] == 1)
        blue++;
    else{
        n /= 2;
        func(x, y, n);
        func(x + n, y, n);
        func(x, y + n, n);
        func(x + n, y + n, n);
    }
}
int main(){
    scanf("%d", &N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++)
            scanf("%d", &arr[i][j]);
    }
    func(0, 0, N);
    printf("%d\n%d\n", white, blue);
}