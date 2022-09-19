/* 
NIM : 18221071
Nama : Ahmad Rizki
Tanggal : 4 September 2022
Topik Praktikum : Pengenalan C
Deskripsi : konversi detik ke jam menit detik   
*/

#include <stdio.h>

int main(){
    int s;
    scanf("%d", &s);
    int jj,mm,ss;
    jj = s/3600;
    mm = (s%3600) / 60;
    ss = (s%3600) % 60;
    printf("%d detik = %d jam %d menit %d detik\n", s, jj, mm, ss);
    return 0;
}