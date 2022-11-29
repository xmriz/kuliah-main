#include <stdio.h>
#include "mesinkarakter.h"

char currentChar;
boolean EOP;

static FILE * pita;
static int retval;

int hitungkarakter(char karakter){
    int count = 0;
    START();
    while (!IsEOP()){
        if (GetCC() == karakter){
            count++;
        }
        ADV();
    }
    return count;
}