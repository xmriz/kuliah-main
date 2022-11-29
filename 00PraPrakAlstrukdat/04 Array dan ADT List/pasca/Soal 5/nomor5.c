/*
NIM : 18221161
Nama : Reyhan Putra Ananda
Tanggal : 30 September 2022
Topik Praktikum : ADT list dan array
Deskripsi : Program
*/

#include <stdio.h>
#include <stdlib.h>

int main () {
    // Input N sebagai jumlah bilangan dalam array
    int N;
    scanf("%d", &N);

    // Buat array dengan jumlah N bilangan
    int * array = (int*)malloc(sizeof(int) * N);

    // Input bilangan sebanyak N dan masukkan satu per satu ke array
    int i;
    int masukan;
    for (i = 0; i < N; i++) {
        scanf("%d", &masukan);
        array[i] = masukan;
    }

    // Input q sebagai jumlah query
    int q;
    scanf("%d", &q);

    // Input batas dan jumlahkan bilangan dengan batas tersebut
    int j, k, l, r;
    for (j = 0; j < q; j++) {
        long hasil = 0;
        scanf("%d %d", &l, &r);
        int k;
        for (k = l-1; k < r; k++) {
            hasil += array[k % N];
        }
        printf("%d\n", hasil);
    }
    free(array);
}