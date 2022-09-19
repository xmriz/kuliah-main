#include <stdio.h>
#include "panjangstring.h"

int panjangString(char*x){
    int i=0;
    while(x[i]!='\0'){
        i++;
    }
    return i;
}