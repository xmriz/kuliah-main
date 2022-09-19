/* 
NIM : 18221071
Nama : Ahmad Rizki
Tanggal : 4 September 2022
Topik Praktikum : Pengenalan C
Deskripsi : Buatlah program dalam Bahasa C yang mengimplementasikan fungsi penjumlahan 2 bilangan bulat
*/

#include <stdio.h>

long long add (long long a, long long b){
    return a + b;
}

int main(){
    long long a, b;
    scanf("%lld %lld", &a,&b);
    long long ans = add(a,b);
    printf("%lld\n", ans);
    return 0;
}