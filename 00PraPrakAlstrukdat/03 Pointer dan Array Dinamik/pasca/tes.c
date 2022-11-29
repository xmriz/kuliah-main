#include <stdio.h>

void f(int x){
    x = 5;
}

int main (){
    int x = 10;
    f(&x);
    printf("%d",x);
}