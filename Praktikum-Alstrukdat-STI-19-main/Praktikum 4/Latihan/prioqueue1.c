#include<stdio.h>
#include"prioqueue.h"
#include<stdlib.h>
/* ********* Prototype ********* */
boolean IsEmpty (Queue Q){
/* Mengirim true jika Q kosong: lihat definisi di atas */
    return (Head(Q)==Nil)&&(Tail(Q)==Nil);
}
boolean IsFull (Queue Q){
/* Mengirim true jika tabel penampung elemen Q sudah penuh */
/* yaitu mengandung elemen sebanyak MaxEl */
    if (Tail(Q)>Head(Q)){
        return ((Tail(Q)-Head(Q))+1)==MaxEl(Q);
    }
    else{
        return (Head(Q)-Tail(Q)==1);
    }
}
int NBElmt (Queue Q){
/* Mengirimkan banyaknya elemen queue. Mengirimkan 0 jika Q kosong. */
    if (Tail(Q)>Head(Q)){
        return ((Tail(Q)-Head(Q))+1);
    }
    else{
        return (Tail(Q)+MaxEl(Q)+1-Head(Q));
    }
}
/* *** Kreator *** */
void CreateEmpty (Queue * Q, int Max){
/* I.S. sembarang */
/* F.S. Sebuah Q kosong terbentuk dan salah satu kondisi sbb: */
/* Jika alokasi berhasil, Tabel memori dialokasi berukuran Max+1 */
/* atau : jika alokasi gagal, Q kosong dg MaxEl=0 */
/* Proses : Melakukan alokasi, membuat sebuah Q kosong */
    (*Q).T=(infotype*)malloc(Max*sizeof(infotype));
    Head(*Q)=Nil;
    Tail(*Q)=Nil;
    MaxEl(*Q)=Max;
}
/* *** Destruktor *** */
void DeAlokasi(Queue * Q){
/* Proses: Mengembalikan memori Q */
/* I.S. Q pernah dialokasi */
/* F.S. Q menjadi tidak terdefinisi lagi, MaxEl(Q) diset 0 */
    free(Q->T);
}
/* *** Primitif Add/Delete *** */
void Add (Queue * Q, infotype X){
/* Proses: Menambahkan X pada Q dengan aturan priority queue, terurut mengecil berdasarkan prio */
/* I.S. Q mungkin kosong, tabel penampung elemen Q TIDAK penuh */
/* F.S. X menjadi TAIL yang baru, TAIL "maju" dengan mekanisme circular buffer;
        elemen baru disisipkan pada posisi yang tepat sesuai dengan prioritas */
    if (IsEmpty(*Q)){
        Head(*Q)+=1;
        Tail(*Q)+=1;
        InfoTail(*Q)=X;
        InfoHead(*Q)=X;
    }
    else{
        Tail(*Q)=(Tail(*Q)+1)%MaxEl(*Q);
        InfoTail(*Q)=X;
    }
}
void Del (Queue * Q, infotype * X){
/* Proses: Menghapus X pada Q dengan aturan FIFO */
/* I.S. Q tidak mungkin kosong */
/* F.S. X = nilai elemen HEAD pd I.S., HEAD "maju" dengan mekanisme circular buffer; 
        Q mungkin kosong */
    *X=InfoHead(*Q);
    if (Head(*Q)==Tail(*Q)){
        Head(*Q)=Nil;
        Tail(*Q)=Nil;
    }
    else{
        Head(*Q)=(Head(*Q)+1)%MaxEl(*Q);
    }
}
/* Operasi Tambahan */
void PrintQueue (Queue Q){
/* Mencetak isi queue Q ke layar */
/* I.S. Q terdefinisi, mungkin kosong */
/* F.S. Q tercetak ke layar dengan format:
<prio-1> <elemen-1>
...
<prio-n> <elemen-n>
#
*/
    while (Head(Q)!=Tail(Q)){
        printf("%d,%d\n",Prio(InfoHead(Q)),Info(InfoHead(Q)));
        Head(Q)=(Head(Q)+1)%MaxEl(Q);
    }
}

