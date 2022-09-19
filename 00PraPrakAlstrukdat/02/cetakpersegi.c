#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    int x = (2*n)-1;
    int i = 0;
    char a='O';
    int j = 0;
    while (i != x*x){
        printf("%c",a);
        i++;
        j++;
        if (a == 'O'){
            a = 'X';
        }
        else if (a == 'X'){
            a = 'O';
        }
        if (j == x){
            printf("\n");
            j=0;
        }
    }
    return 0;
}