#include <stdio.h>

void ubah(int *x){
    *x = 21;
}

int main(){
    int p = 20;
    ubah(&p);
    printf("%d", p);
}