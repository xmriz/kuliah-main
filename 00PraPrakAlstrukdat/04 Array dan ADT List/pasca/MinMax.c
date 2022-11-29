#include <stdio.h>
#include "MinMax.h"

List MinMax(List L){
    List L2;
    L2 = MakeList();
    ElType P = First(L);
    int min = Get(P);
    int max = Get(P);
    while (P != Mark){
        if (Get(P) < min){
            min = Get(P);
        }
        if (Get(P) > max){
            max = Get(P);
        }
        P = Next(P);
    }
    InsertFirst(&L2, max);
    InsertFirst(&L2, min);
    return L2;
}