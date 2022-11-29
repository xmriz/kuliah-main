#include <stdio.h>
#include "garis.h"

void MakeGARIS(POINT P1, POINT P2, GARIS *L)
{
    PAwal(*L) = P1;
    PAkhir(*L) = P2;
}

void BacaGARIS(GARIS *L){
    POINT p1,p2;
    BacaPOINT(&p1);
    BacaPOINT(&p2);
    while (EQ(p1,p2)){
        printf("Garis tidak valid\n");
        BacaPOINT(&p1);
        BacaPOINT(&p2);
    }
    MakeGARIS(p1,p2,L); //karena parameternya pointer, maka tidak perlu ditulis &, karena sudah otomatis mengambil alamat dari L
}

void TulisGARIS(GARIS L){
    printf("((%.2f,%.2f),",Absis(PAwal(L)),Ordinat(PAwal(L)));
    printf("(%.2f,%.2f))",Absis(PAkhir(L)),Ordinat(PAkhir(L)));
}

float PanjangGARIS(GARIS L){
    return Panjang(PAwal(L),PAkhir(L));
}

float Gradien(GARIS L){
    return (Ordinat(PAkhir(L))-Ordinat(PAwal(L)))/(Absis(PAkhir(L))-Absis(PAwal(L)));
}

boolean IsTegakLurus(GARIS L1, GARIS L2){
    return (Gradien(L1)*Gradien(L2)==-1);
}

boolean IsSejajar(GARIS L1, GARIS L2){
    return (Gradien(L1)==Gradien(L2));
}


