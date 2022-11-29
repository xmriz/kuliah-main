#include <stdio.h>
#include <stdlib.h>
#include "OddEvenList.h"

int main(){
    List L, Odd, Even;
    CreateEmpty(&L);
    CreateEmpty(&Odd);
    CreateEmpty(&Even);
    int input;
    scanf("%d", &input);
    while(input != -999){
        InsertLast(&L, Alokasi(input));
        scanf("%d", &input);
    }
    OddEvenList(L, &Odd, &Even);
    PrintInfo(Odd);
    printf("\n");
    PrintInfo(Even);
    printf("\n");
    return 0;
}