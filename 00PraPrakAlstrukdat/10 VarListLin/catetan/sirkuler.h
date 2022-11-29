#include "boolean.h"

#define NIL NULL
typedef int ElType;
typedef struct node *address;
typedef struct node
{
    ElType info;
    address next;
} Node;
/* Definisi list: */
/* List kosong: FIRST(l) = NIL */
/* Setiap elemen dengan address p dapat diacu INFO(p), NEXT(p) */
/* Elemen terakhir list: jika addressnya last,
maka NEXT(last) = FIRST(l) */
typedef struct
{
    address first;
} List;
/* Selektor */
#define INFO(p) (p)->info
#define NEXT(p) (p)->next
#define FIRST(l) ((l).first)


boolean addrSearch(List l, address p);
/* Mencari apakah ada elemen list l yang beralamat p */
/* Mengirimkan true jika ada, false jika tidak ada */
void insertFirst(List *l, ElType x);
/* I.S. List l terdefinisi */
/* F.S. Menambahkan elemen bernilai x sebagai elemen pertama */
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
/* F.S. x adalah elemen terakhir list sebelum penghapusan */
/*      Elemen list berkurang satu (mungkin menjadi kosong) */
/*      Last element baru adalah predesesor elemen pertama yg lama, jika ada */
void displayList(List l);
/* I.S. List l mungkin kosong */
/* F.S. Jika list tidak kosong, semua nilai (info) yg disimpan pada elemen list diprint */
/*      Jika list kosong, hanya menuliskan "list kosong" */



