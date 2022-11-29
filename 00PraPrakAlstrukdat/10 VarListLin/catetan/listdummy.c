#include <stdio.h>
#include "listdummy.h"

boolean isEmpty(List l)
{
    /* Mengirim true jika list kosong */
    /* Kamus Lokal */
    /* Algoritma */
    return (FIRST(l) == LAST(l));
}

void CreateList(List *l)
{
    /* I.S. Sembarang */
    /* F.S. Terbentuk list l kosong, dengan satu elemen dummy,
    jika alokasi dummy berhasil */
    /*      Jika gagal maka FIRST(l) = LAST(l) = NIL dan list gagal terbentuk */
    /* Kamus Lokal */
    address pDummy;
    /* Algoritma */
    pDummy = alokasi(0); /* INFO(pDummy) tidak didefinisikan */
    if (pDummy != Nil)
    {
        FIRST(*l) = pDummy;
        LAST(*l) = pDummy;
    }
    else /* List gagal terbentuk */
    {
        FIRST(*l) = Nil;
        LAST(*l) = Nil;
    }
}

int indexOf(List l, ElType x)
{
    /* Mengembalikan indeks node list dengan nilai X, atau IDX_UNDEF jika tidak ada */
    /* Kamus Lokal */
    address p;
    int idx;
    /* Algoritma */
    INFO(LAST(l)) = x; /* letakkan X di sentinel */
    p = FIRST(l);
    idx = 0;
    while (INFO(p) != x)
    {
        p = NEXT(p);
        idx++;
    } /* INFO(p) = x */
    if (p != LAST(l))
    { /* bukan ketemu di sentinel */
        return idx;
    }
    else /* p = LAST(l), ketemu di sentinel */
    {
        return IDX_UNDEF;
    }
}

void insertFirst(List *l, ElType x)
{
    /* I.S. List l terdefinisi */
    /* F.S. Menambahkan elemen x sebagai elemen pertama List l */
    /* Kamus Lokal */
    address p;
    /* Algoritma */
    p = newNode(x);
    if (p != Nil)
    {
        NEXT(p) = FIRST(*l);
        FIRST(*l) = p;
    }
}

void insertLast(List *l, ElType x)
{
    /* I.S. List l terdefinisi */
    /* F.S. x ditambahkan sebagai elemen terakhir l yang baru */
    /* Alamat elemen dummy tidak berubah */
    /* Kamus Lokal */
    address p, last;
    /* Algoritma */
    if (isEmpty(*l))
    {
        insertFirst(l, x);
    }
    else
    {
        p = newNode(x);
        if (p != Nil)
        {
            last = FIRST(*l);
            while (NEXT(last) != LAST(*l))
            {
                last = NEXT(last);
            } /* NEXT(last) == LAST(*l) alias dummy */
            NEXT(last) = p;
            NEXT(p) = LAST(*l);
        }
    }
}

void insertLast(List *l, ElType x)
{
    /* I.S. List l terdefinisi */
    /* F.S. x ditambahkan sebagai elemen terakhir l yang baru */
    /* Versi jika alamat elemen dummy boleh berubah */
    /* Kamus Lokal */
    address p;
    /* Algoritma */

    if (isEmpty(*l))
    {
        insertFirst(l, x);
    }
    else
    {
        INFO(LAST(*l)) = x;
        p = newNode(x); /* dummy baru */
        if (p != Nil)
        {
            NEXT(LAST(*l)) = p;
            LAST(*l) = p;
        }
    }
}

void deleteFirst(List *l, ElType *x)
{
    /* I.S. List l tidak kosong */
    /* F.S. x adalah elemen pertama list l sebelum penghapusan */
    /*      Elemen list berkurang satu (mungkin menjadi kosong) */
    /*      First element yg baru adalah suksesor elemen pertama yang lama */
    /* Kamus Lokal */
    address p;
    /* Algoritma */
    p = FIRST(*l);
    *x = INFO(p);
    FIRST(*l) = NEXT(FIRST(*l));
    free(p);
}

void deleteLast(List *l, ElType *x)
{
    /* I.S. List l tidak kosong */
    /* F.S. x adalah elemen terakhir list l sebelum penghapusan */
    /*      Elemen list berkurang satu (mungkin menjadi kosong) */
    /*      Last element baru adalah predesesor elemen terakhir yg lama, jika ada*/
    /* Kamus Lokal */
    address last, precLast;
    /* Algoritma */
    last = FIRST(*l);
    precLast = Nil;
    while (NEXT(last) != LAST(*l))
    {
        precLast = last;
        last = NEXT(last);
    }
    *x = INFO(last);
    if (precLast == Nil)
    { /* kasus satu elemen */
        FIRST(*l) = LAST(*l);
    }
    else
    {
        NEXT(precLast) = LAST(*l);
    }
    free(last);
}


