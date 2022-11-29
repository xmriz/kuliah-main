#include "mesinkarakterv2.h"
#include "mesinkata.h"
#include "boolean.h"
#include <stdio.h>

boolean EndWord;
Word currentWord;

/*  Menerima sebuah parameter string bertipe string
    Mengirimkan panjang sebuah string */
int stringLength (char* string){
    int i=0;
    while(string[i] != '\0'){
        i++;
    }
    return i;
}

/*  Menerima sebuah paramater command bertipe string
    Mengirimkan kata yang elemen of arraynya berasal dari command */
Word toKata(char* command){
    Word kata;
    int i=0;
    while (i<stringLength(command)){
        kata.TabWord[i] = command[i];
        i++;
    }    
    kata.Length = i;
    return kata;
}

/*  Menerima dua buah parameter yaitu string1 dan string2
    Mengembalikan true apabila string2 merupakan anagram dari string1
    Mengembalikan false apabila string2 bukan merupakan anagram dari string1
    String dianggap anagram apabila disusun dari huruf yang tepat sama */
boolean isAnagram(Word string1, Word string2){
    int i,j;
    int count_a;
    int count_b;
    char karakter;
    boolean sama = false;
    if (string1.Length == string2.Length){
        sama = true;
        for (i=0;i<string1.Length;i++){
            count_a = 0;
            count_b = 0;
            karakter = string1.TabWord[i];
            for(j=0;j<string1.Length;j++){
                if (string1.TabWord[j]== karakter){
                    count_a +=1;
                }
                if (string2.TabWord[j] == karakter){
                    count_b +=1;
                }
            }
            if (count_a != count_b){
                sama = false;
                break;
            }
        }
    }
return sama;
}

/*  Mengembalikan jumlah frekuensi kemunculan anagram alstrukdat 
    pada argumen frek */
void anagramalstrukdat(int* frek){
    char *string = "alstrukdat";
    Word kata;
    kata = toKata(string);
    STARTWORD();
    *frek = 0;
    while(!(isEndWord())){
        if (isAnagram(kata,currentWord)){
            *frek +=1;
        }
        ADVWORD();
    }
}
