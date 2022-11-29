#include "queue.h"

Queue tanpaBomb(Queue queue, ElType bomb){
	int value;
	int i=IDX_HEAD(q);
	for(i;i!=IDX_TAIL(q)+1; i=(i+1)%CAPACITY){
		if(queue.buffer[i] != bomb){
			dequeue(&queue,&value);
			enqueue(&queue,value);
		}
	}
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
