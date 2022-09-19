#include"lat_arraydin.h"
#include<stdio.h>
#include<stdlib.h>
void MakeEmpty(TabInt *T, int maxel){
/* I.S. T sembarang, maxel > 0 */
/* F.S. Terbentuk tabel T kosong dengan kapasitas maxel */
    TI(*T)=(ElType*)malloc(maxel*sizeof(ElType));
    MaxEl(*T)=maxel;
    Neff(*T)=0;
}

void Dealokasi(TabInt *T){
/* I.S. T terdefinisi; */
/* F.S. TI(T) dikembalikan ke system, MaxEl(T)=0; Neff(T)=0 */
    free(TI(*T));
    MaxEl(*T)=0;
    Neff(*T)=0;
}

/* ********** SELEKTOR (TAMBAHAN) ********** */
/* *** Banyaknya elemen *** */
int NbElmt(TabInt T){
/* Mengirimkan banyaknya elemen efektif tabel */
/* Mengirimkan nol jika tabel kosong */
/* *** Daya tampung container *** */
    return Neff(T);
}
int MaxElement(TabInt T){
/* Mengirimkan maksimum elemen yang dapat ditampung oleh tabel */
/* *** Selektor INDEKS *** */
    return MaxEl(T);
}
IdxType GetFirstIdx(TabInt T){
/* Prekondisi : Tabel T tidak kosong */
/* Mengirimkan indeks elemen T pertama */
    return IdxMin;
}
IdxType GetLastIdx(TabInt T){
/* Prekondisi : Tabel T tidak kosong */
/* Mengirimkan indeks elemen T terakhir */
    return IdxMin+Neff(T)-1;
}

/* ********** Test Indeks yang valid ********** */
boolean IsIdxValid(TabInt T, IdxType i){
/* Mengirimkan true jika i adalah indeks yang valid utk ukuran tabel */
/* yaitu antara indeks yang terdefinisi utk container*/
    return (i>=IdxMin && i<=MaxEl(T));
}
boolean IsIdxEff(TabInt T, IdxType i){
/* Mengirimkan true jika i adalah indeks yang terdefinisi utk tabel */
/* yaitu antara FirstIdx(T)..LastIdx(T) */
    return (IdxMin<=i && i<=GetLastIdx(T));
}

/* ********** TEST KOSONG/PENUH ********** */
/* *** Test tabel kosong *** */
boolean IsEmpty(TabInt T){
/* Mengirimkan true jika tabel T kosong, mengirimkan false jika tidak */
/* *** Test tabel penuh *** */
    return Neff(T)==0;
}
boolean IsFull(TabInt T){
/* Mengirimkan true jika tabel T penuh, mengirimkan false jika tidak */
    return Neff(T)==MaxEl(T);
}

/* ********** BACA dan TULIS dengan INPUT/OUTPUT device ********** */
/* *** Mendefinisikan isi tabel dari pembacaan *** */
void BacaIsi(TabInt *T){
/* I.S. T sembarang dan sudah dialokasikan sebelumnya */
/* F.S. Tabel T terdefinisi */
/* Proses : membaca banyaknya elemen T dan mengisi nilainya */
/* 1. Baca banyaknya elemen diakhiri enter, misalnya N */
/*    Pembacaan diulangi sampai didapat N yang benar yaitu 0 <= N <= MaxElement(T) */
/*    Jika N tidak valid, tidak diberikan pesan kesalahan */
/* 2. Jika 0 < N <= MaxElement(T); Lakukan N kali: Baca elemen mulai dari indeks
      IdxMin satu per satu diakhiri enter */
/*    Jika N = 0; hanya terbentuk T kosong */
    int N;
    IdxType i;
    do{
        scanf("%d",&N);
    }while (N<0 || N>MaxElement(*T));
    MakeEmpty(T,N);
    for (i=GetFirstIdx(*T);i<N;i++){
        ElType temp;
        scanf("%d",&temp);
        Elmt(*T,i)=temp;
        Neff(*T)++;
    }
}
void TulisIsiTab(TabInt T){
/* Proses : Menuliskan isi tabel dengan traversal, tabel ditulis di antara kurung siku;
   antara dua elemen dipisahkan dengan separator "koma", tanpa tambahan karakter di depan,
   di tengah, atau di belakang, termasuk spasi dan enter */
/* I.S. T boleh kosong */
/* F.S. Jika T tidak kosong: [e1,e2,...,en] */
/* Contoh : jika ada tiga elemen bernilai 1, 20, 30 akan dicetak: [1,20,30] */
/* Jika tabel kosong : menulis [] */
    if(Neff(T)==0){
        printf("[]");
    }
    else{
        IdxType i;
        printf("[");
        for (i=GetFirstIdx(T);i<Neff(T);i++){
            printf("%d",Elmt(T,i));
        }
        printf("]");
    }
}

/* ********** OPERATOR ARITMATIKA ********** */
/* *** Aritmatika tabel : Penjumlahan, pengurangan, perkalian, ... *** */
TabInt PlusMinusTab(TabInt T1, TabInt T2, boolean plus);
/* Prekondisi : T1 dan T2 memiliki Neff sama dan tidak kosong */
/* Jika plus = true, mengirimkan  T1+T2, yaitu setiap elemen T1 dan T2 pada indeks yang sama dijumlahkan */
/* Jika plus = false, mengirimkan T1-T2, yaitu setiap elemen T1 dikurangi elemen T2 pada indeks yang sama */

/* ********** OPERATOR RELASIONAL ********** */
/* *** Operasi pembandingan tabel : < =, > *** */
boolean IsEQ(TabInt T1, TabInt T2){
    if (Neff(T1)!=Neff(T2)){
        return false;
    }
    else{
        boolean beda=true;
        IdxType i;
        for (i=GetFirstIdx(T1);i<Neff(T1);i++){
            if (Elmt(T1,i)!=Elmt(T2,i)){
                beda=false;
            }
        }
        return beda;
    }
}
/* Mengirimkan true jika T1 sama dengan T2 yaitu jika Neff T1 = T2 dan semua elemennya sama */

/* ********** SEARCHING ********** */
/* ***  Perhatian : Tabel boleh kosong!! *** */
IdxType Search1(TabInt T, ElType X){
/* Search apakah ada elemen tabel T yang bernilai X */
/* Jika ada, menghasilkan indeks i terkecil, dengan elemen ke-i = X */
/* Jika tidak ada, mengirimkan IdxUndef */
/* Menghasilkan indeks tak terdefinisi (IdxUndef) jika tabel T kosong */
/* Skema Searching yang digunakan bebas */
    if (IsEmpty(T)){
        return IdxUndef;
    }
    else{
        boolean nope=true;
        IdxType i=GetFirstIdx(T),j;
        while (nope && i<GetLastIdx(T)){
            if (Elmt(T,i)==X){
                nope=false;
                j=i;
            }
            i++;
        }
        if (nope==true){
            return j;
        }
        else{
            return IdxUndef;
        }
    }
}
boolean SearchB(TabInt T, ElType X){
/* Search apakah ada elemen tabel T yang bernilai X */
/* Jika ada, menghasilkan true, jika tidak ada menghasilkan false */
/* Skema searching yang digunakan bebas */
    if (IsEmpty(T)){
        return false;
    }
    else{
        IdxType i=GetFirstIdx(T);
        boolean beda=true;
        while (beda&&i<GetLastIdx(T)){
            if(Elmt(T,i)==X){
                beda=false;
            }
        }
        return !beda;
    }
}

/* ********** NILAI EKSTREM ********** */
void MaxMin(TabInt T, ElType *Max, ElType *Min);
/* I.S. Tabel T tidak kosong */
/* F.S. Max berisi nilai maksimum T;
        Min berisi nilai minimum T */

/* ********** OPERASI LAIN ********** */
void CopyTab(TabInt Tin, TabInt *Tout);
/* I.S. Tin terdefinisi tidak kosong, Tout sembarang */
/* F.S. Tout berisi salinan dari Tin (identik, Neff dan MaxEl sama) */
/* Proses : Menyalin isi Tin ke Tout */
ElType SumTab(TabInt T);
/* Menghasilkan hasil penjumlahan semua elemen T */
/* Jika T kosong menghasilkan 0 */
int CountX(TabInt T, ElType X);
/* Menghasilkan berapa banyak kemunculan X di T */
/* Jika T kosong menghasilkan 0 */
boolean IsAllGenap(TabInt T);
/* Menghailkan true jika semua elemen T genap. T boleh kosong */

/* ********** SORTING ********** */
void Sort(TabInt *T, boolean asc){
/* I.S. T boleh kosong */
/* F.S. Jika asc = true, T terurut membesar */
/*      Jika asc = false, T terurut mengecil */
/* Proses : Mengurutkan T dengan salah satu algoritma sorting,
   algoritma bebas */
    IdxType i,j;
    if (asc=true){
        for (i=GetFirstIdx(*T);i<Neff(*T);i++){
            for (j=GetFirstIdx(*T);j<Neff(*T)-1;j++){
                if (Elmt(*T,j)>Elmt(*T,j+1)){
                    ElType temp=Elmt(*T,j);
                    Elmt(*T,j)=Elmt(*T,j+1);
                    Elmt(*T,j+1)=temp;
                }
            }
        }
    }
    else{
        for (i=GetFirstIdx(*T);i<Neff(*T);i++){
            for (j=GetFirstIdx(*T);j<Neff(*T)-1;j++){
                if (Elmt(*T,j)<Elmt(*T,j+1)){
                    ElType temp=Elmt(*T,j);
                    Elmt(*T,j)=Elmt(*T,j+1);
                    Elmt(*T,j+1)=temp;
                }
            }
        }
    }
}

/* ********** MENAMBAH DAN MENGHAPUS ELEMEN DI AKHIR ********** */
/* *** Menambahkan elemen terakhir *** */
void AddAsLastEl(TabInt *T, ElType X){
/* Proses: Menambahkan X sebagai elemen terakhir tabel */
/* I.S. Tabel T boleh kosong, tetapi tidak penuh */
/* F.S. X adalah elemen terakhir T yang baru */
    if(IsEmpty(*T)){
        Neff(*T)++;
        Elmt(*T,0)=X;
    }
    else{
        Neff(*T)++;
        Elmt(*T,GetLastIdx(*T)+1)=X;
    }
}
/* ********** MENGHAPUS ELEMEN ********** */
void DelLastEl(TabInt *T, ElType *X){
/* Proses : Menghapus elemen terakhir tabel */
/* I.S. Tabel tidak kosong */
/* F.S. X adalah nilai elemen terakhir T sebelum penghapusan, */
/*      Banyaknya elemen tabel berkurang satu */
/*      Tabel T mungkin menjadi kosong */
    Neff(*T)--;
    *X=Elmt(*T,GetLastIdx(*T));
}
/* ********* MENGUBAH UKURAN ARRAY ********* */
void GrowTab(TabInt *T, int num){
/* Proses : Menambahkan max element sebanyak num */
/* I.S. Tabel sudah terdefinisi */
/* F.S. Ukuran tabel bertambah sebanyak num */
    int temp[Neff(*T)],max,eff;
    max=MaxEl(*T);
    eff=Neff(*T);
    IdxType i=GetFirstIdx(*T);
    
    for (i=GetFirstIdx(*T);i<Neff(*T);i++){
        temp[i]=Elmt(*T,i);
    }
    Dealokasi(T);
    MakeEmpty(T,num+max);
    for (i=GetFirstIdx(*T);i<eff;i++){
        Elmt(*T,i)=temp[i];
    }
    Neff(*T)=eff;
}

void ShrinkTab(TabInt *T, int num){
/* Proses : Mengurangi max element sebanyak num */
/* I.S. Tabel sudah terdefinisi, ukuran MaxEl > num, dan Neff < MaxEl - num. */
/* F.S. Ukuran tabel berkurang sebanyak num. */
    int temp[Neff(*T)],min,eff;
    min=MaxEl(*T);
    eff=Neff(*T);
    IdxType i=GetFirstIdx(*T);
    for (i=GetFirstIdx(*T);i<Neff(*T);i++){
        temp[i]=Elmt(*T,i);
    }
    Dealokasi(T);
    MakeEmpty(T,min-num);
    for (i=GetFirstIdx(*T);i<eff;i++){
        Elmt(*T,i)=temp[i];
    }
    Neff(*T)=eff;
}
void CompactTab(TabInt *T){
/* Proses : Mengurangi max element sehingga Neff = MaxEl */
/* I.S. Tabel tidak kosong */
/* F.S. Ukuran MaxEl = Neff */
    int temp[Neff(*T)],j,eff;
    eff=Neff(*T);
    IdxType i=GetFirstIdx(*T);
    for (i=GetFirstIdx(*T);i<Neff(*T);i++){
        temp[i]=Elmt(*T,i);
    }
    Dealokasi(T);
    MakeEmpty(T,eff);
    for (i=GetFirstIdx(*T);i<eff;i++){
        Elmt(*T,i)=temp[i];
    }
    Neff(*T)=eff;
}