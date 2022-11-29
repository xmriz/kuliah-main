#include "stack.h"
#include <string.h>
#include <stdio.h>

void hitungstack(Stack* S1,Stack* S2,Stack* S3){
    //S1 > S2
    int bil1,bil2,hasil;
    int ctr = 0;
    int k = 0;
    while((S2->TOP != Nil)){
            Pop(S2,&bil2);
            Pop(S1,&bil1);
            if(bil2 > bil1){
                bil1 +=10;
                if (S1->T[S1->TOP] == 0){
                    while (S1->T[S1->TOP - k] == 0){
                        S1->T[S1->TOP - k] +=9;
                        k++;
                    }
                    S1->T[S1->TOP - k] -=1;
                }
                else{
                    S1->T[S1->TOP] -=1;
                }
            }
            hasil = bil1 - bil2;
            Push(S3,hasil);
        }
        while (S1->TOP != Nil){
            Pop(S1,&hasil);
            Push(S3,hasil);
        }
        while(S3->TOP != Nil){
            Pop(S3,&hasil);
            if((hasil == 0)&&(ctr > 0)){
                printf("%d",hasil);
                ctr++;
            }
            else if (hasil != 0){
                printf("%d",hasil);
                ctr++;
            }
        }
        printf("\n");
}

int main(){
    Stack Sa,Sb,Sc;
    CreateEmpty(&Sa);
    CreateEmpty(&Sb);
    CreateEmpty(&Sc);
    int i;
    int k = 0;
    int bil1, bil2;
    char S1[100];
    char S2[100];
    scanf("%s",S1);
    scanf("%s",S2);
    for(i=0;i<strlen(S1);i++){
        bil1 = S1[i] - '0';
        Push(&Sa,bil1);
    }
    for(i=0;i<strlen(S2);i++){
        bil2 = S2[i] - '0';
        Push(&Sb,bil2);
    }
    if(strlen(S1) > strlen(S2)){
        hitungstack(&Sa,&Sb,&Sc);
    }
    else if(strlen(S2)>strlen(S1)){
        printf("-");
        hitungstack(&Sb,&Sa,&Sc);
    }
    else if(strlen(S1) == strlen(S2)){
        while((S1[k]==S2[k])&&(k<strlen(S1) - 1)){
            k+=1;
        }
        if(S1[k] > S2[k]){
            hitungstack(&Sa,&Sb,&Sc);
        }
        else if(S2[k] > S1[k]){
            printf("-");
            hitungstack(&Sb,&Sa,&Sc);
        }
        else if (S2[k] == S1[k]){
            printf("%d\n",0);
        }
    }
    return 0;
}