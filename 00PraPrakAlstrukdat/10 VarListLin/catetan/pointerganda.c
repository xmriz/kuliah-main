#include <stdio.h>
#include "pointerganda.h"

void insertFirst(List *l, ElType x)
{
    /* I.S. List l terdefinisi */
    /* F.S. Menambahkan elemen baru x sebagai elemen pertama */
    /* Kamus Lokal */
    address p;
    /* Algoritma */
    p = newNode(x);
    if (p != NIL)
    {
        NEXT(p) = FIRST(*l);
        if (!isEmpty(*l))
        {
            PREV(FIRST(*l)) = p;
        }
        else /* l kosong */
        {
            LAST(*l) = p;
        }
        FIRST(*l) = p;
    }
}

void insertLast(List *l, ElType x)
{
    /* I.S. List l terdefinisi */
    /* F.S. x ditambahkan sebagai elemen terakhir l yang baru */
    /* Kamus Lokal */
    address p;
    /* Algoritma */
    p = newNode(x);
    if (p != NIL)
    {
        PREV(p) = LAST(*l);
        if (!isEmpty(*l))
        {
            NEXT(LAST(*l)) = p;
        }
        else /* l kosong */
        {
            FIRST(*l) = p;
        }
        LAST(*l) = p;
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
    if (FIRST(*l) == LAST(*l))
    { /* l hanya 1 elemen */
        LAST(*l) = NIL;
    }
    else
    { /* l > 1 elemen */
        PREV(NEXT(FIRST(*l))) = NIL;
    }
    FIRST(*l) = NEXT(FIRST(*l));
    free(P);
}

void deleteLast(List *l, ElType *x)
{
    /* I.S. List l tidak kosong */
    /* F.S. x adalah elemen terakhir list l sebelum penghapusan */
    /*      Elemen list berkurang satu (mungkin menjadi kosong) */
    /*      Last element baru adalah predesesor elemen pertama yg lama, jika ada */
    /* Kamus Lokal */
    address p;
    /* Algoritma */
    p = LAST(*l);
    *x = INFO(p);
    if (FIRST(*l) == LAST(*l))
    { /* l hanya 1 elemen */
        FIRST(*l) = NIL;
    }
    else
    { /* L > 1 elemen */
        NEXT(PREV(LAST(*l))) = NIL;
    }
    LAST(*l) = PREV(LAST(*l));
    free(p);
}
