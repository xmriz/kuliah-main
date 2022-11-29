/*
NIM : 18221161
Nama : Reyhan Putra Ananda
Tanggal : 25 September 2022
Topik Praktikum : Pointer dan Array Dinamik
Deskripsi : Implementasi fibonacci.h
*/

// Deret bilangan fibonacci adalah deret angka yang susunan angkanya
// merupakan penjumlahan dari dua angka sebelumnya.
// Contoh:
// Fib 0: 1
// Fib 1: 1
// Fib 2: 1 + 1 = 2
// Fib 3: 2 + 1 = 3
// Fib 4: 3 + 2 = 5
// Fib 5: 5 + 3 = 8

#include<stdio.h>
#include"fibonacci.h"
// Menerima argument sebuah integer n dan mengembalikan
// nilai suku ke-n dari deret fibonacci ke argumen result
// Contoh:
// n = 5
// Nilai argumen result = 8
void fibonacci1(int n, int *result){
    int i;
    if ((n==0) || (n==1)){
        *result = 1;
    }
    else{
        int a = 1;
        int b = 1;
        for(i=2;i<=n;i++){
            *result = a+b;
            a = b;
            b = *result;
        }
    } 
}

// Menerima argument sebuah integer n dan mengembalikan
// nilai suku ke-n dari deret fibonacci
int fibonacci2(int n){
    int result;
    fibonacci1(n,&result);
    return result;
}

// Menerima argument sebuah integer n
// Output adalah argumen result yang bertipe pointer int digunakan sebagai array
// Tuliskan semua nilai deret fibonacci dari 0 - n ke argumen result
// n = 5
// result = [1, 1, 2, 3, 5, 8]
void fibonacci3(int n, int *result){
    int i;
    int a = 0;
    int b = 1;
    result[0] = 1;
    if (n>=1){
        for (i=1;i<=n;i++){
            result[i] = a+b;
            a = b;
            b = result[i];
        } 
    }
}