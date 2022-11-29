#include <stdio.h>
#include "boolean.h"
#include "OddEvenList.h"


void OddEvenList(List L, List *Odd, List *Even){
    CreateEmpty(Odd);
    CreateEmpty(Even);
    address P = First(L);
    while(P != Nil){
        if(Info(P) % 2 == 0){
            InsertLast(Even, Alokasi(Info(P)));
        } else{
            InsertLast(Odd, Alokasi(Info(P)));
        }
        P = Next(P);
    }
    int temp;
    //sort ascending Odd
    if (!IsEmpty(*Odd)){
        address P1 = First(*Odd);
        while(P1 != Nil){
            address P2 = Next(P1);
            while(P2 != Nil){
                if(Info(P1) > Info(P2)){
                    temp = Info(P1);
                    Info(P1) = Info(P2);
                    Info(P2) = temp;
                }
                P2 = Next(P2);
            }
            P1 = Next(P1);
        }
    }
    //sort descending Even
    if (!IsEmpty(*Even)){
        address P1 = First(*Even);
        while(P1 != Nil){
            address P2 = Next(P1);
            while(P2 != Nil){
                if(Info(P1) > Info(P2)){
                    temp = Info(P1);
                    Info(P1) = Info(P2);
                    Info(P2) = temp;
                }
                P2 = Next(P2);
            }
            P1 = Next(P1);
        }
    }
}
    /* Memisahkan elemen ganjil dan genap dari list L kedalam dua list baru secara mengurut membesar*/
    /* I.S: List L TIDAK mungkin kosong dan memiliki nilai lebih dari sama dengan 0(value>=0), List Odd dan Even kosong*/
    /* F.S: List Odd memiliki elemen bernilai ganjil mengurut membesar, List Even memiliki elemen bernilai genap mengurut membesar
            List L TIDAK PERLU DIDEALOKASI*/
    /*Contoh:
        Input:
            L: [0,3,1,4,5]
            Odd: []
            Even: []
        Output:
            L: [0,3,1,4,5]
            Odd: [1,3,5]
            Even: [0,4] */
    /*Note: 
        1. Bilangan 0 merupakan bilangan genap
        2. Buatlah List Odd dan Even terlebih dahulu*/
 