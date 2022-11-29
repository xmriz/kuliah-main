/*
NIM : 18221161
Nama : Reyhan Putra Ananda
Tanggal : 30 September 2022
Topik Praktikum : ADT list dan array
Deskripsi : Implementasi MinMax.h
*/

#include <stdio.h>
#include "MinMax.h"

List MinMax(List L) {
    ElType nilaiMin = L.A[FirstIdx(L)];
    IdxType idxNilaiMin = FirstIdx(L);
    IdxType j;
    for (j = FirstIdx(L); j <= Length(L) - 1; j++) {
        if (L.A[j] < nilaiMin) {
            nilaiMin = L.A[j];
            idxNilaiMin = j;
        }
    }
    DeleteAt(&L, idxNilaiMin);
    InsertLast(&L, nilaiMin);
    ElType nilaiMax = L.A[FirstIdx(L)];
    IdxType idxNilaiMax = FirstIdx(L);
    IdxType i;
    for (i = FirstIdx(L); i <= Length(L) - 1; i++) {
        if (L.A[i] > nilaiMax) {
            nilaiMax = L.A[i];
            idxNilaiMax = i;
        }
    }
    DeleteAt(&L, idxNilaiMax);
    InsertLast(&L, nilaiMax);
    return L; 
}