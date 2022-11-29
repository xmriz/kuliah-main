#include "circular_queue.h"
#include "reverse.h"

void transferReverse(Queue* q1, Queue* q2){
    int i,j,n;
    n = Length(*q1);
    for(i=0;i<n;i++){
        for(j=q1->HEAD;j!=q1->TAIL;j=(j+1)%q1->MaxEl){
            Push(q1,Pop(q1));
        }
        Push(q2,Pop(q1));
    }
}

// Proses: Memindahkan tiap elemen q1 ke q2 dengan urutan yang terbalik
// I.S.: q1 tidak kosong, q2 kosong. q1 dan q2 memiliki panjang yang sama
// F.S.: q1 kosong, q2 berisi elemen-elemen yang tadinya milik q1 dengan urutan yang terbalik