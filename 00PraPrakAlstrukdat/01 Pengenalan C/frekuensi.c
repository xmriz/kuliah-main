#include <stdio.h>

int main(){
    char Tab[10];
    int N[10];
    int k=0;
    for (k; k<10; k++){
        N[k] = 0;
    }
    scanf("%s", &Tab);
    int i=0;
    for (i; i<10; i++){
        if (Tab[i] == '0'){
            N[0] += 1;
        }
        else if (Tab[i] == '1'){
            N[1] += 1;
        }
        else if (Tab[i] == '2'){
            N[2] += 1;
        }
        else if (Tab[i] == '3'){
            N[3] += 1;
        }
        else if (Tab[i] == '4'){
            N[4] += 1;
        }
        else if (Tab[i] == '5'){
            N[5] += 1;
        }
        else if (Tab[i] == '6'){
            N[6] += 1;
        }
        else if (Tab[i] == '7'){
            N[7] += 1;
        }
        else if (Tab[i] == '8'){
            N[8] += 1;
        }
        else if (Tab[i] == '9'){
            N[9] += 1;
        }
    }
    int j=0;
    for (j; j<10; j++){
        printf("%d", N[j]);
    }
    printf("\n");
    return 0;
}