#include <stdio.h>
#include <stdlib.h>
#include "listsirkuler.h"

/* PROTOTYPE */
/****************** TEST LIST KOSONG ******************/
boolean IsEmpty (List L){
    return (First(L) == Nil);
}
/* Mengirim true jika list kosong. Lihat definisi di atas. */

/****************** PEMBUATAN LIST KOSONG ******************/
void CreateEmpty (List *L){
    First(*L) = Nil;
}
/* I.S. L sembarang             */
/* F.S. Terbentuk list kosong. Lihat definisi di atas. */

/****************** Manajemen Memori ******************/
address Alokasi (infotype X){
    address P = (address) malloc(sizeof(ElmtList));
    if (P != Nil){
        Info(P) = X;
        Next(P) = Nil;
    }
    return P;
}
/* Mengirimkan address hasil alokasi sebuah elemen */
/* Jika alokasi berhasil, maka address tidak nil, dan misalnya */
/* menghasilkan P, maka Info(P)=X, Next(P)=Nil */
/* Jika alokasi gagal, mengirimkan Nil */
void Dealokasi (address P){
    free(P);
}
/* I.S. P terdefinisi */
/* F.S. P dikembalikan ke sistem */
/* Melakukan dealokasi/pengembalian address P */

/****************** PENCARIAN SEBUAH ELEMEN LIST ******************/
address Search (List L, infotype X){
    address P = First(L);
    if (P != Nil){
        do {
            if (Info(P) == X){
                return P;
            }
            P = Next(P);
        } while (P != First(L));
    }
    return Nil;
}
/* Mencari apakah ada elemen list dengan Info(P)= X */
/* Jika ada, mengirimkan address elemen tersebut. */
/* Jika tidak ada, mengirimkan Nil */

/****************** PRIMITIF BERDASARKAN NILAI ******************/
/*** PENAMBAHAN ELEMEN ***/
void InsVFirst (List *L, infotype X){
    address P = Alokasi(X);
    if (P != Nil){
        if (IsEmpty(*L)){
            First(*L) = P;
            Next(P) = P;
        } else {
            address Last = First(*L);
            while (Next(Last) != First(*L)){
                Last = Next(Last);
            }
            Next(P) = First(*L);
            First(*L) = P;
            Next(Last) = P;
        }
    }
}
/* I.S. L mungkin kosong */
/* F.S. Melakukan alokasi sebuah elemen dan */
/* menambahkan elemen pertama dengan nilai X jika alokasi berhasil */
void InsVLast (List *L, infotype X){
    address P = Alokasi(X);
    if (P != Nil){
        if (IsEmpty(*L)){
            First(*L) = P;
            Next(P) = P;
        } else {
            address Last = First(*L);
            while (Next(Last) != First(*L)){
                Last = Next(Last);
            }
            Next(Last) = P;
            Next(P) = First(*L);
        }
    }
}
/* I.S. L mungkin kosong */
/* F.S. Melakukan alokasi sebuah elemen dan */
/* menambahkan elemen list di akhir: elemen terakhir yang baru */
/* bernilai X jika alokasi berhasil. Jika alokasi gagal: I.S.= F.S. */

/*** PENGHAPUSAN ELEMEN ***/
void DelVFirst (List *L, infotype * X){
    if (!IsEmpty(*L)){
        address P = First(*L);
        *X = Info(P);
        if (Next(P) == P){
            First(*L) = Nil;
        } else {
            address Last = First(*L);
            while (Next(Last) != First(*L)){
                Last = Next(Last);
            }
            First(*L) = Next(P);
            Next(Last) = First(*L);
        }
        Dealokasi(P);
    }
}
/* I.S. List L tidak kosong  */
/* F.S. Elemen pertama list dihapus: nilai info disimpan pada X */
/*      dan alamat elemen pertama di-dealokasi */
void DelVLast (List *L, infotype * X){
    if (!IsEmpty(*L)){
        address P = First(*L);
        if (Next(P) == P){
            *X = Info(P);
            First(*L) = Nil;
        } else {
            address Last = First(*L);
            while (Next(Next(Last)) != First(*L)){
                Last = Next(Last);
            }
            P = Next(Last);
            *X = Info(P);
            Next(Last) = First(*L);
        }
        Dealokasi(P);
    }
}
/* I.S. list tidak kosong */
/* F.S. Elemen terakhir list dihapus: nilai info disimpan pada X */
/*      dan alamat elemen terakhir di-dealokasi */

/****************** PRIMITIF BERDASARKAN ALAMAT ******************/
/*** PENAMBAHAN ELEMEN BERDASARKAN ALAMAT ***/
void InsertFirst (List *L, address P){
    if (P != Nil){
        if (IsEmpty(*L)){
            First(*L) = P;
            Next(P) = P;
        } else {
            address Last = First(*L);
            while (Next(Last) != First(*L)){
                Last = Next(Last);
            }
            Next(P) = First(*L);
            First(*L) = P;
            Next(Last) = P;
        }
    }
}
/* I.S. Sembarang, P sudah dialokasi  */
/* F.S. Menambahkan elemen ber-address P sebagai elemen pertama */
void InsertLast (List *L, address P){
    if (P != Nil){
        if (IsEmpty(*L)){
            First(*L) = P;
            Next(P) = P;
        } else {
            address Last = First(*L);
            while (Next(Last) != First(*L)){
                Last = Next(Last);
            }
            Next(Last) = P;
            Next(P) = First(*L);
        }
    }
}
/* I.S. Sembarang, P sudah dialokasi  */
/* F.S. P ditambahkan sebagai elemen terakhir yang baru */
void InsertAfter (List *L, address P, address Prec){
    if (P != Nil){
        if (IsEmpty(*L)){
            First(*L) = P;
            Next(P) = P;
        } else {
            Next(P) = Next(Prec);
            Next(Prec) = P;
        }
    }
}
/* I.S. Prec pastilah elemen list dan bukan elemen terakhir, */
/*      P sudah dialokasi  */
/* F.S. Insert P sebagai elemen sesudah elemen beralamat Prec */

/*** PENGHAPUSAN SEBUAH ELEMEN ***/
void DelFirst (List *L, address *P){
    if (!IsEmpty(*L)){
        *P = First(*L);
        if (Next(*P) == *P){
            First(*L) = Nil;
        } else {
            address Last = First(*L);
            while (Next(Last) != First(*L)){
                Last = Next(Last);
            }
            First(*L) = Next(*P);
            Next(Last) = First(*L);
        }
    }
}
/* I.S. List tidak kosong */
/* F.S. P adalah alamat elemen pertama list sebelum penghapusan */
/*      Elemen list berkurang satu (mungkin menjadi kosong) */
/* First element yg baru adalah suksesor elemen pertama yang lama */
void DelLast (List *L, address *P){
    if (!IsEmpty(*L)){
        *P = First(*L);
        if (Next(*P) == *P){
            First(*L) = Nil;
        } else {
            address Last = First(*L);
            while (Next(Next(Last)) != First(*L)){
                Last = Next(Last);
            }
            *P = Next(Last);
            Next(Last) = First(*L);
        }
    }
}
/* I.S. List tidak kosong */
/* F.S. P adalah alamat elemen terakhir list sebelum penghapusan  */
/*      Elemen list berkurang satu (mungkin menjadi kosong) */
/* Last element baru adalah predesesor elemen pertama yg lama, */
/* jika ada */
void DelAfter (List *L, address *Pdel, address Prec){
    if (!IsEmpty(*L)){
        *Pdel = Next(Prec);
        if (Next(*Pdel) == *Pdel){
            First(*L) = Nil;
        } else {
            Next(Prec) = Next(*Pdel);
        }
    }
}
/* I.S. List tidak kosong. Prec adalah anggota list  */
/* F.S. Menghapus Next(Prec): */
/*      Pdel adalah alamat elemen list yang dihapus  */
void DelP (List *L, infotype X){
    if (!IsEmpty(*L)){
        address P = First(*L);
        if (Info(P) == X){
            if (Next(P) == P){
                First(*L) = Nil;
            } else {
                address Last = First(*L);
                while (Next(Last) != First(*L)){
                    Last = Next(Last);
                }
                First(*L) = Next(P);
                Next(Last) = First(*L);
            }
            Dealokasi(P);
        } else {
            address Last = First(*L);
            while (Next(Last) != First(*L)){
                Last = Next(Last);
            }
            while (Next(P) != First(*L) && Info(Next(P)) != X){
                P = Next(P);
            }
            if (Next(P) != First(*L)){
                address Pdel = Next(P);
                Next(P) = Next(Pdel);
                Dealokasi(Pdel);
            }
        }
    }
}
/* I.S. Sembarang */
/* F.S. Jika ada elemen list beraddress P, dengan Info(P)=X  */
/* Maka P dihapus dari list dan di-dealokasi */
/* Jika tidak ada elemen list dengan Info(P)=X, maka list tetap */
/* List mungkin menjadi kosong karena penghapusan */

/****************** PROSES SEMUA ELEMEN LIST ******************/
void PrintInfo (List L){
    if (IsEmpty(L)){
        printf("[]");
    } else {
        address P = First(L);
        printf("[");
        do {
            printf("%d", Info(P));
            P = Next(P);
            if (P != First(L)){
                printf(",");
            }
        } while (P != First(L));
        printf("]");
    }
}
/* I.S. List mungkin kosong */
/* F.S. Jika list tidak kosong, iai list dicetak ke kanan: [e1,e2,...,en] */
/* Contoh : jika ada tiga elemen bernilai 1, 20, 30 akan dicetak: [1,20,30] */
/* Jika list kosong : menulis [] */
/* Tidak ada tambahan karakter apa pun di awal, akhir, atau di tengah */

