#include <stdio.h>

int main(){
    int x;
    scanf("%x",&x);
    if (x%2==0){
        if ((x/2)%2==0){
            printf("Ya\n");
        } else {
            printf("Tidak\n");
        }
    } else {
        printf("Tidak\n");
    }
    return 0;
}