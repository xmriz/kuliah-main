/*
NAMA: Marcelino Feihan
NIM: 18219006
TANGGAL: 12 November 2020
TOPIK: Praktikum 8
DESKRIPSI: Listdp.c
*/

#include"listdp.h"
#include<stdio.h>
#include<stdlib.h>
/* PROTOTYPE */
/****************** TEST LIST KOSONG ******************/
boolean IsEmpty (List L){
/* Mengirim true jika list kosong. Lihat definisi di atas. */
    return ((First(L)==Nil)&&(Last(L)==Nil));
}
/****************** PEMBUATAN LIST KOSONG ******************/
void CreateEmpty (List *L){
/* I.S. L sembarang  */
/* F.S. Terbentuk list kosong. Lihat definisi di atas. */
    First(*L)=Nil;
    Last(*L)=Nil;
}

/****************** Manajemen Memori ******************/
address Alokasi (infotype X){
/* Mengirimkan address hasil alokasi sebuah elemen */
/* Jika alokasi berhasil, maka address tidak nil. */
/* Misalnya: menghasilkan P, maka Info(P)=X, Next(P)=Nil, Prev(P)=Nil */
/* Jika alokasi gagal, mengirimkan Nil. */
    ElmtList *P=(ElmtList*)malloc(sizeof(ElmtList));
    if(P!=Nil){
        Info(P)=X;
        Prev(P)=Nil;
        Next(P)=Nil;
        return P;
    }
    else
    {
        return Nil;
    }
    
}
void Dealokasi (address P){
/* I.S. P terdefinisi */
/* F.S. P dikembalikan ke sistem */
/* Melakukan dealokasi/pengembalian address P */
    free(P);
}

/****************** PENCARIAN SEBUAH ELEMEN LIST ******************/
address Search (List L, infotype X){
/* Mencari apakah ada elemen list dengan Info(P)=X */
/* Jika ada, mengirimkan address elemen tersebut. */
/* Jika tidak ada, mengirimkan Nil */
    address check=Nil;
    if (!IsEmpty(L)){
        address P;
        P=First(L);
        while((Info(P)!=X)&&(Next(P)!=Nil)){
            P=Next(P);
        }
        if(Info(P)==X){
            check=P;
        }
    }
    return check;
}

/****************** PRIMITIF BERDASARKAN NILAI ******************/
/*** PENAMBAHAN ELEMEN ***/
void InsVFirst (List *L, infotype X){
/* I.S. L mungkin kosong */
/* F.S. Melakukan alokasi sebuah elemen dan */
/* menambahkan elemen pertama dengan nilai X jika alokasi berhasil */
    address P=Alokasi(X);
    if(P!=Nil){
        InsertFirst(L,P);
    }
}
void InsVLast (List *L, infotype X){
/* I.S. L mungkin kosong */
/* F.S. Melakukan alokasi sebuah elemen dan */
/* menambahkan elemen list di akhir: elemen terakhir yang baru */
/* bernilai X jika alokasi berhasil. Jika alokasi gagal: I.S.= F.S. */
    address P=Alokasi(X);
    if(P!=Nil){
        InsertLast(L,P);
    }
}

/*** PENGHAPUSAN ELEMEN ***/
void DelVFirst (List *L, infotype *X){
/* I.S. List L tidak kosong  */
/* F.S. Elemen pertama list dihapus: nilai info disimpan pada X */
/*      dan alamat elemen pertama di-dealokasi */
    address P;
    DelFirst(L,&P);
    *X=Info(P);
    Dealokasi(P);
}
void DelVLast (List *L, infotype *X){
/* I.S. list tidak kosong */
/* F.S. Elemen terakhir list dihapus: nilai info disimpan pada X */
/*      dan alamat elemen terakhir di-dealokasi */
    address P;
    DelLast(L,&P);
    *X=Info(P);
    Dealokasi(P);
}
/****************** PRIMITIF BERDASARKAN ALAMAT ******************/
/*** PENAMBAHAN ELEMEN BERDASARKAN ALAMAT ***/
void InsertFirst (List *L, address P){
/* I.S. Sembarang, P sudah dialokasi  */
/* F.S. Menambahkan elemen ber-address P sebagai elemen pertama */
    if(IsEmpty(*L)){
        First(*L)=P;
        Last(*L)=P;
    }
    else{
        InsertBefore(L,P,First(*L));
    }
}
void InsertLast (List *L, address P){
/* I.S. Sembarang, P sudah dialokasi  */
/* F.S. P ditambahkan sebagai elemen terakhir yang baru */
    if(IsEmpty(*L)){
        InsertFirst(L,P);
    }
    else{
        InsertAfter(L,P,Last(*L));
    }
}
void InsertAfter (List *L, address P, address Prec){
/* I.S. Prec pastilah elemen list; P sudah dialokasi  */
/* F.S. Insert P sebagai elemen sesudah elemen beralamat Prec */
    Prev(P)=Prec;
    Next(P)=Next(Prec);
    Next(Prec)=P;
    if(Next(P)==Nil){
        Last(*L)=P;
    }
    else{
        Prev(Next(P))=P;
    }
    

}
void InsertBefore (List *L, address P, address Succ){
/* I.S. Succ pastilah elemen list; P sudah dialokasi  */
/* F.S. Insert P sebagai elemen sebelum elemen beralamat Succ */
    Prev(P)=Prev(Succ);
    Next(P)=Succ;
    Prev(Succ)=P;
    if(Prev(P)==Nil){
        First(*L)=P;
    }
    else{
        Next(Prev(P))=P;
    }
    
}

/*** PENGHAPUSAN SEBUAH ELEMEN ***/
void DelFirst (List *L, address *P){
/* I.S. List tidak kosong */
/* F.S. P adalah alamat elemen pertama list sebelum penghapusan */
/*      Elemen list berkurang satu (mungkin menjadi kosong) */
/* First element yg baru adalah suksesor elemen pertama yang lama */
    *P=First(*L);
    if(First(*L)==Last(*L)){
        First(*L)=Nil;
        Last(*L)=Nil;
    }
    else{
        First(*L)=Next(First(*L));
        Prev(First(*L))=Nil;
    }
    Next(*P)=Nil;
    Prev(*P)=Nil;
}
void DelLast (List *L, address *P){
/* I.S. List tidak kosong */
/* F.S. P adalah alamat elemen terakhir list sebelum penghapusan  */
/*      Elemen list berkurang satu (mungkin menjadi kosong) */
/* Last element baru adalah predesesor elemen pertama yg lama, jika ada */
    *P=Last(*L);
    if(First(*L)==Last(*L)){
        First(*L)=Nil;
        Last(*L)=Nil;
    }
    else{
        Last(*L)=Prev(Last(*L));
        Next(Last(*L))=Nil;
    }
    Next(*P)=Nil;
    Prev(*P)=Nil;
}
void DelP (List *L, infotype X){
/* I.S. Sembarang */
/* F.S. Jika ada elemen list beraddress P, dengan Info(P)=X  */
/* maka P dihapus dari list dan didealokasi */
/* Jika tidak ada elemen list dengan Info(P)=X, maka list tetap */
/* List mungkin menjadi kosong karena penghapusan */
    address cari=Search(*L,X);
    if(cari!=Nil){
        address P=First(*L),prec=Nil;
        while (P!=cari){
            prec=P;
            P=Next(P);
        }
        if(prec==Nil){
            DelFirst(L,&cari);
        }
        else{
            DelAfter(L,&cari,prec);
        }
    }
}
void DelAfter (List *L, address *Pdel, address Prec){
/* I.S. List tidak kosong. Prec adalah anggota list. */
/* F.S. Menghapus Next(Prec): */
/*      Pdel adalah alamat elemen list yang dihapus  */
    *Pdel=Next(Prec);
    if(Next(*Pdel)==Nil){
        Next(Prec)=Nil;
        Last(*L)=Prec;
    }
    else{
        Next(Prec)=Next(*Pdel);
        Prev(Next(*Pdel))=Prec;
    }
    Prev(*Pdel)=Nil;
    Next(*Pdel)=Nil;
}
void DelBefore (List *L, address *Pdel, address Succ){
/* I.S. List tidak kosong. Succ adalah anggota list. */
/* F.S. Menghapus Prev(Succ): */
/*      Pdel adalah alamat elemen list yang dihapus  */
    *Pdel=Prev(Succ);
    if(Prev(*Pdel)==Nil){
        Prev(Succ)=Nil;
        First(*L)=Succ;
    }
    else{
        Prev(Succ)=Prev(*Pdel);
        Next(Prev(*Pdel))=Succ;
    }
    Prev(*Pdel)=Nil;
    Next(*Pdel)=Nil;
}

/****************** PROSES SEMUA ELEMEN LIST ******************/
void PrintForward (List L){
/* I.S. List mungkin kosong */
/* F.S. Jika list tidak kosong, isi list dicetak dari elemen pertama */
/* ke elemen terakhir secara horizontal ke kanan: [e1,e2,...,en] */
/* Contoh : jika ada tiga elemen bernilai 1, 20, 30 akan dicetak: [1,20,30] */
/* Jika list kosong : menulis [] */
/* Tidak ada tambahan karakter apa pun di awal, akhir, atau di tengah */
    if (IsEmpty(L)){
        printf("[]");
    }
    else{
        address P=First(L);
        printf("[");
        while(P!=Nil){
            if(P==Last(L)){
                printf("%d",Info(P));
            }
            else{
                printf("%d,",Info(P));
            }
            P=Next(P);
        }
        printf("]");
    }
}
void PrintBackward (List L){
/* I.S. List mungkin kosong */
/* F.S. Jika list tidak kosong, isi list dicetak dari elemen terakhir */
/* ke elemen pertama secara horizontal ke kanan: [en,en-1,...,e2,e1] */
/* Contoh : jika ada tiga elemen bernilai 1, 20, 30 akan dicetak: [30,20,1] */
/* Jika list kosong : menulis [] */
/* Tidak ada tambahan karakter apa pun di awal, akhir, atau di tengah */
    if (IsEmpty(L)){
        printf("[]");
    }
    else{
        address P=Last(L);
        printf("[");
        while(P!=Nil){
            if(P==First(L)){
                printf("%d",Info(P));
            }
            else{
                printf("%d,",Info(P));
            }
            P=Prev(P);
        }
        printf("]");
    }
}

