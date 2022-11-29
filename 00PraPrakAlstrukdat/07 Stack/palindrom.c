#include <stdio.h>
#include "stack.h"

int main(){
    Stack S1,S2,tempS;
    CreateEmpty(&S1);
    CreateEmpty(&S2);
    CreateEmpty(&tempS);
    int val;
    scanf("%d",&val);
    while (val != 0){
        Push(&S1, val);
        Push(&tempS, val);
        scanf("%d",&val);
    }
    if (IsEmpty(S1)){
        printf("Stack kosong\n");
    } else {
        int X;
        int i=0;
        for (i;i<Top(S1)+1;i++){
            Pop(&tempS,&X);
            Push(&S2, X);
        }
        boolean isPalindrom = true;
        int j=0;
        for (j;j<Top(S1)+1;j++){
            if (S1.T[j] != S2.T[j]){
                isPalindrom = false;
            }
        }
        if (isPalindrom == true){
            printf("Palindrom\n");
        } else {
            printf("Bukan Palindrom\n");
        }
    }
    return 0;
}