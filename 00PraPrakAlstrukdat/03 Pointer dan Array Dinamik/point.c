#include <stdio.h>
#include <math.h>
#include "point.h"

// POINT MakePOINT
POINT MakePOINT(float x, float y){
    POINT p1;
    Absis(p1) = x;
    Ordinat(p1) = y;
    return p1;
}

// void BacaPoint
void BacaPOINT(POINT *P){
    float x,y;
    scanf("%f %f", &x, &y);
    *P = MakePOINT(x,y);
}

// void TulisPoint
void TulisPOINT(POINT P){
    printf("(%.2f,%.2f)", Absis(P), Ordinat(P));
}

// boolean EQ
boolean EQ (POINT P1, POINT P2){
    return ((Absis(P1) == Absis(P2)) && (Ordinat(P1) == Ordinat(P2)));
}

// boolean NEQ
boolean NEQ(POINT P1, POINT P2){
    return !(EQ(P1,P2));
}

// boolean isOrigin
boolean IsOrigin(POINT P){
    return ((Absis(P) == 0) && (Ordinat(P) == 0));
}

// boolean IsOnSbX
boolean IsOnSbX(POINT P){
    return (Ordinat(P) == 0);
}

// boolean IsOnSbY
boolean IsOnSbY(POINT P){
    return (Absis(P) == 0);
}

// int Kuadran
int Kuadran(POINT P){
    if (Absis(P) > 0 && Ordinat(P) > 0) {
        return 1;
    } 
    else if (Absis(P) < 0 && Ordinat(P) > 0){
        return 2;
    }
    else if (Absis(P) < 0 && Ordinat(P) < 0){
        return 3;
    }
    else {
        return 4;
    }
}

// POINT PlusDelta
POINT PlusDelta(POINT P, float deltaX, float deltaY){
    POINT copyP;
    copyP = MakePOINT((Absis(P) + deltaX), (Ordinat(P) + deltaY));
    return copyP;
}

// void Geser
void Geser(POINT *P, float deltaX, float deltaY){
    Absis(*P) += deltaX;
    Ordinat(*P) += deltaY;
}

// float Jarak0
float Jarak0 (POINT P){
    return sqrtf((Absis(P)*Absis(P)) + (Ordinat(P)*Ordinat(P)));
}

// float Panjang
float Panjang(POINT P1, POINT P2){
    return sqrtf(powf(Absis(P1)-Absis(P2), 2) + (powf(Ordinat(P1)-Ordinat(P2), 2)));
}