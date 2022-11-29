/* File: prioqueuelist.c */
#include <stdio.h>
#include "prioqueuelist.h"

/* Prototype manajemen memori */
address newNode(ElType x, int pr){
    address P = (address) malloc(sizeof(Node));
    if(P != Nil){
        INFO(P) = x;
        PRIO(P) = pr;
        NEXT(P) = Nil;
    }
    return P;
}
/* Mengembalikan alamat sebuah Node hasil alokasi dengan info = x dan prio = pr,
atau NIL jika alokasi gagal */

void delNode(address P){
    free(P);
}
/* I.S. P adalah hasil alokasi, P != Nil */
/* F.S. Alamat P didealokasi, dikembalikan ke sistem */

boolean isEmpty(PrioQueue q){
    return ADDR_HEAD(q) == Nil;
}
/* Mengirim true jika q kosong: ADDR_HEAD(q)=NIL and ADDR_TAIL(q)=NIL */

int length(PrioQueue q){
    int count = 0;
    address P = ADDR_HEAD(q);
    while(P != Nil){
        count++;
        P = NEXT(P);
    }
    return count;
}
/* Mengirimkan banyaknya elemen queue. Mengirimkan 0 jika q kosong */
/*** Kreator ***/

void CreateQueue(PrioQueue *q){
    ADDR_HEAD(*q) = Nil;
}
/* I.S. sembarang */
/* F.S. Sebuah q kosong terbentuk */
/*** Primitif Enqueue/Dequeue ***/

void enqueue(PrioQueue *q, ElType x, int pr){
    address P = newNode(x, pr);
    if(P != Nil){
        if(isEmpty(*q)){
            ADDR_HEAD(*q) = P;
        }
        else {
            address Q = ADDR_HEAD(*q);
            if(PRIO(P) > PRIO(Q)){
                NEXT(P) = Q;
                ADDR_HEAD(*q) = P;
            }
            else {
                while (NEXT(Q) != Nil && PRIO(P) <= PRIO(NEXT(Q))){ // priority paling tinggi di depan
                    Q = NEXT(Q);
                }
                NEXT(P) = NEXT(Q);
                NEXT(Q) = P;
            }
        }
    }
}
/* Proses: Mengalokasi x dengan prio pr dan menambahkan x pada q
jika alokasi berhasil; jika alokasi gagal q tetap */

/* I.S. q mungkin kosong */
/* F.S. x menjadi elemen q sesuai dengan urutan prioritas */

void dequeue(PrioQueue *q, ElType *x, int *pr){
    if(!isEmpty(*q)){
        address P = ADDR_HEAD(*q);
        *x = INFO(P);
        *pr = PRIO(P);
        ADDR_HEAD(*q) = NEXT(P);
        delNode(P);
    }
}
/* Proses: Menghapus x pada bagian HEAD dari q dan mendealokasi elemen HEAD */
/* Pada dasarnya operasi deleteFirst */
/* I.S. q tidak mungkin kosong */
/* F.S. x = nilai elemen HEAD pd I.S., HEAD "mundur" */
