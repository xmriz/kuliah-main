#include <stdio.h>

int main(){
    int N;
    scanf("N : %d", N);
    if (N % 2 != 0){
        printf("inputan N salah");
    }
    else {
        int stars = 1;
        int spaces = (N-stars)/2;
        do {
            for (int i = 0; i<spaces; i++){
                printf(" ");
            }

            for (int i = 0; i<stars; i++){
                printf("*");
            }
            for (int i = 0; i<spaces; i++){
                printf(" ");
            }
        } while ( i <= (N/2)+1)
    }
    return 0;
}
