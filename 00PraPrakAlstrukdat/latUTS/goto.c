#include <stdio.h>

int f(int *p){
    *p = (*p) * 2;
    return *p;
}

int main(){
    int x = 2;
    printf("%d", f(&x));
    return 0;
}