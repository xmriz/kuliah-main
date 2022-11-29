#include "mesinkarakter.h"

int hitungfrekuensi(){
    int count = 0;
    START();
    while(!(IsEOP())){
        if ((currentChar == 'T') || (currentChar=='t')){
            ADV();
            if ((currentChar == 'I') || (currentChar=='i')){
                ADV();
                if ((currentChar == 'G') || (currentChar=='g')){
                    ADV();
                    if ((currentChar == 'A') || (currentChar=='a')){
                        count +=1;
                        ADV();
                    }
                }
            }
        }
        else{
            ADV();
        }
    }
    return count;
}