#include "listlinier.h"
#include <stdio.h>
int main(){
    int input = 1;
    boolean valid = false;
    List L;
    CreateEmpty(&L);
    while(input<=100 && input>=0){
        scanf("%d",&input);
        if(input<=100 && input >=0){
            InsertLast(&L,Alokasi(input));
        }
    }
    if(IsEmpty(L)){
        printf("Daftar nilai kosong\n");
    } else{
        printf("%d\n",NbElmt(L));
        printf("%d\n",Max(L));
        printf("%d\n",Min(L));
        printf("%.2f\n",Average(L));
        PrintInfo(L);
        printf("\n");
        InversList(&L);
        PrintInfo(L);
        printf("\n");
    }
}