#include <stdio.h>
#include "jumlahkonsonanvokal.h"

int main(){
    int k,v;
    char x[30] = "ai-ueo";
    jumlahKonsonanVokal(x,&k,&v);
    printf("%d\n%d\n",k,v);
}