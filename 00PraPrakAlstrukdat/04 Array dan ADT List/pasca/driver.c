#include <stdio.h>  
#include "arrayMhs.h"

int main(){
    TabMhs T;
    MakeEmpty(&T);
    T.Neff = 1;
    T.TI[1].nama = "A";
    T.TI[1].nim = "1";
    T.TI[1].nilai = 32.333;
    TulisIsi(T);
    return 0;
}