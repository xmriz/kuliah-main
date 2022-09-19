#include <stdio.h>
#include <string.h>

int isDivided7(int x){
    return (x%7==0);
}

int isThere7 (int x){
    char intToChar[100];
    sprintf(intToChar, "%d", x);
    int n = strlen(intToChar);
    int i;
    int is7=0;
    for (i=0;i<n;i++){
        if (intToChar[i] == '7'){
            is7 = 1;
            break;
        }
    }
    return is7;

}

int main(){
    int n;
    int num;
    scanf("%d", &n);
    int j,k;
    for (j=0;j<n;j++){
        scanf("%d", &num);
        int sum = 0;
        for (k=1;k<=num;k++){
            if ((isDivided7(k) || (isThere7(k)))){
                sum += k;
            }
        }
        printf("%d\n", sum);
    }
    return 0;
}