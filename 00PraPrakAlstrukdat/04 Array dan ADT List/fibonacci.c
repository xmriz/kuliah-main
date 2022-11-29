#include <stdio.h>
#include "fibonacci.h"

void fibonacci1(int n, int *result){
    if (n == 0){
        *result = 1;
    }
    else if (n == 1){
        *result = 1;
    }
    else{
        int a, b;
        fibonacci1(n-1, &a);
        fibonacci1(n-2, &b);
        *result = a + b;
    }
}

int fibonacci2(int n){
    int result;
    fibonacci1(n, &result);
    return result;
}


void fibonacci3(int n, int *result){
    int i;
    for (i = 0; i <= n; i++){
        fibonacci1(i, &result[i]);
    }
}