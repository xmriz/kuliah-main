#include <stdio.h>
#include "arraydin.h"

// Konstruktor
ArrayDin MakeArrayDin(){
    ArrayDin array;
    array.A = (ElType *) malloc(InitialSize * sizeof(ElType));
    array.Capacity = InitialSize;
    array.Neff = 0;
    return array;
}

// Destruktor
void DeallocateArrayDin(ArrayDin *array){
    free(array->A);
}

// Fungsi untuk mengetahui apakah suatu array kosong.
boolean IsEmpty(ArrayDin array){
    return array.Neff == 0;
}

// Fungsi untuk mendapatkan banyaknya elemen efektif array, 0 jika tabel kosong.
int Length(ArrayDin array){
    return array.Neff;
}

// Mengembalikan elemen array L yang ke-I (indeks lojik).
ElType Get(ArrayDin array, IdxType i){
    return array.A[i];
}

// Fungsi untuk mendapatkan kapasitas yang tersedia.
int GetCapacity(ArrayDin array){
    return array.Capacity;
}

// Fungsi untuk menambahkan elemen baru di index ke-i
void InsertAt(ArrayDin *array, ElType el, IdxType i){
    if (array->Neff == array->Capacity){
        array->Capacity *= 2;
        array->A = (ElType *) realloc(array->A, array->Capacity * sizeof(ElType));
    }
    for (int j = array->Neff; j > i; j--){
        array->A[j] = array->A[j-1];
    }
    array->A[i] = el;
    array->Neff++;
}

// Fungsi untuk menghapus elemen di index ke-i ArrayDin
void DeleteAt(ArrayDin *array, IdxType i){
    for (int j = i; j < array->Neff-1; j++){
        array->A[j] = array->A[j+1];
    }
    array->Neff--;
}