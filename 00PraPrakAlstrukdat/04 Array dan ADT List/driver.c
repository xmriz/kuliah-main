#include <stdio.h>
#include "fibonacci.h"

int main(){
    int n;
    scanf("%d", &n);
    int result[n+1];
    fibonacci3(n, result);
    int i;
    for (i = 0; i <= n; i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}