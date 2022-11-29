#include "boolean.h"

#define NIL NULL
typedef int ElType;
typedef struct node *address;
typedef struct node
{
    ElType info;
    address prev;
    address next;
} Node;
/* Definisi list: */
/* List kosong: First = Nil and Last = Nil */
/* Setiap elemen dengan address P dapat diacu Info(P), Prev(P), Next(P) */
typedef struct
{
    address first;
    address last;
} List;

/* Selektor */
#define INFO(p) (p)->info
#define PREV(p) (p)->prev
#define NEXT(p) (p)->next
#define FIRST(l) ((l).first)
#define LAST(l) ((l).last)


void insertFirst(List *l, ElType x);
/* I.S. List l terdefinisi */
/* F.S. Menambahkan elemen baru x sebagai elemen pertama */
void insertLast(List *l, ElType x);
/* I.S. List l terdefinisi */
/* F.S. x ditambahkan sebagai elemen terakhir l yang baru */
void deleteFirst(List *l, ElType *x);
/* I.S. List l tidak kosong */
/* F.S. x adalah elemen pertama list l sebelum penghapusan */
/*      Elemen list berkurang satu (mungkin menjadi kosong) */
/*      First element yg baru adalah suksesor elemen pertama yang lama */
void deleteLast(List *l, ElType *x);
/* I.S. List l tidak kosong */
/* F.S. x adalah elemen terakhir list l sebelum penghapusan */
/*      Elemen list berkurang satu (mungkin menjadi kosong) */
/*      Last element baru adalah predesesor elemen pertama yg lama, jika ada */
