#include <stdio.h>

int main(){
    int N;
    scanf("%d", &N);
    int arr[N];
    for (int i = 0; i < N; i++){
        scanf("%d", &arr[i]);
    }
    int q;
    scanf("%d", &q);
    for (int j = 0; j<q; j++){
        int a,b;
        scanf("%d %d", &a, &b);
        int count = a;
        int sum = 0;
        int idx;
        while (count <= b){
            idx = (count-1) % N;
            sum += arr[idx];
            count++;
        }
        printf("%d\n", sum);
        }
    return 0;
    }