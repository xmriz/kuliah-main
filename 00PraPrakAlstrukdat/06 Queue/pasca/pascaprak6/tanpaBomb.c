#include "tanpaBomb.h"

Queue tanpaBomb(Queue queue, ElType bomb){
    Queue nobomb;
    int i;
    CreateQueue(&nobomb);
    for (i=queue.idxHead;i<=queue.idxTail;(i+1)%CAPACITY){
        if (queue.buffer[i] != bomb){
            enqueue(&nobomb,bomb);
        }
    }
    return nobomb;
}
/* Mengembalikan sebuah queue yang sudah tidak memiliki nilai bomb */

/*
    Contoh input:
        queue : [2,3,4,5,6] // 2 adalah head, 6 adalah tail
        bomb : 3
    Contoh output: [2,4,5,6]

    Contoh input:
        queue : [2,3,4,5,6] // 2 adalah head, 6 adalah tail
        bomb : 7
    Contoh output: [2,3,4,5,6]

*/