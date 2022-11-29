#include <stdio.h>
#include "jumlahkonsonanvokal.h"

int isAlphabet(char c){
    return ((c>='a' && c<='z') || (c>='A' && c<='Z'));
}

int isVowel(char c){
    return (c=='a' || c=='i' || c=='u' || c=='e' || c=='o' || c=='A' || c=='I' || c=='U' || c=='E' || c=='O');

}

void jumlahKonsonanVokal(char*a, int*k, int*v){
    int i=0;
    *k=0;
    *v=0;
    while (a[i]!='\0'){
        if (isAlphabet(a[i])){
            if (isVowel(a[i])){
                *v+=1;
            }else{
                *k+=1;
            }
        }
        i++;
    }
}