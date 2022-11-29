#include <stdio.h>
#include "queue.h"

int main(){
	int x,max,min,waktu,value,count,c;
	max = 0;
	min = 0;
	count = 0;
	c = 0;
	x = -1;
	while (x != 1){
		scanf("%d",&x);
	}
	Queue q;
	CreateQueue(&q);
	do {
		if(x==1){
			scanf("%d",&waktu);
			if (waktu>0){
				enqueue(&q, waktu);
				c = c + 1;
				}
			if (c==1){
				max = TAIL(q);
				min = HEAD(q);
				}
			}
		else if (x==2){
			if (length(q) > 0){
				count = count +1;
				dequeue(&q,&value);
				if (max < value){
					max = value;
					}
				if (min > value){
					min = value;
					}
				}
			}
		scanf("%d",&x);
		} while (x!=0);
	if (count == 0){
		max = 0;
		min = 0;
	}
	printf("%d\n",count);
	printf("%d\n",min);
	printf("%d\n",max);
	return 0;
}
