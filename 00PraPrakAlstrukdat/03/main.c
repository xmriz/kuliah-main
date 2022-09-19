#include <stdio.h>
#include "point.h"

int main(){
    POINT p = MakePOINT(1,1);
    POINT p0 = MakePOINT(0,0);
    Geser(&p, 1, 1);
    TulisPOINT(p);
    printf("%f", Panjang(p,p0));
    return 0;
}