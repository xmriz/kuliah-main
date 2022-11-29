#include <stdio.h>
#include "copyqueue.h"

// Menyalin queue.
void copyQueue(Queue *queueInput, Queue *queueOutput){
	if (!isEmpty(*queueInput)){
		int value;
		Queue q;
		CreateQueue(&q);
		int a,b,i;
		a = IDX_HEAD(*queueInput);
		b = IDX_TAIL(*queueInput)+1;
		i=a;
		for(i;i!=b; i=(i+1)%CAPACITY){
			dequeue(queueInput,&value);
			enqueue(&q,value);
		}
		int c,d,j;
		c = IDX_HEAD(q);
		d = IDX_TAIL(q)+1;
		j=c;
		for(j;j!=d; j=(j+1)%CAPACITY){
			dequeue(&q,&value);
			enqueue(queueInput,value);
			enqueue(queueOutput,value);
		}
	}
	
}
/* Proses: Menyalin isi dari queueInput ke queueOutput */
/* I.S. queueInput mungkin kosong, tabel penampung elemen queueInput TIDAK penuh */
/* F.S. queueOutput memiliki isi queue yang sama */
/*
    Contoh input:
    queueInput : [2,3,4,5,6] // 2 adalah head, 6 adalah tail
    queueOutput: queue kosong

    Contoh output:
    queueInput:  [2,3,4,5,6]
    queueOutput: [2,3,4,5,6]
*/

/*
    Catatan
    - Hati-hati jangan sampai algoritma Anda mengubah hasil akhir dari queueInput juga.
      Elemen di queueInput harus tetap sama setelah algoritma dijalankan.
    Hint
    - Buat queue baru selain queueInput dan queueOutput untuk tempat penyimpanan
      queueInput sementara.
*/
