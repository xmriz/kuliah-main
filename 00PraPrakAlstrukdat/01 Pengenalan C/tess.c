#include <stdio.h>

int main(){
    int N;
    printf("N : ");
    scanf("%d", &N);
    if (N%2 == 0){
        printf("inputan N salah");
    }
    else {
        int stars = 1;
        int spaces = (N-1)/2;
        for (int i=0; i < N; i++){
            for (int j=0; j < spaces; j++){
                printf(" ");
            }
            for (int j=0; j < stars; j++){
                printf("*");
            }
            printf("\n");
            if (i < N/2){
                stars++;
                stars++;
                spaces--;
            } else {
                stars--; 
                stars--;
                spaces++;
            } 
        }
    }
    return 0;
}