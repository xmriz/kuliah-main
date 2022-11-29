#include <stdio.h>
#include "aritmatika.h"

int main(){
    char x[] = "9423+*5/-";
    int result;
    infotype n = strlen(x);
    result = eval(x,n);
    printf("%d", result);
}