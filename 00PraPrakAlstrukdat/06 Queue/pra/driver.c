#include <stdio.h>
#include "reverse.h"

int main(){
    Queue q1,q2;
    q1 = CreateQueue(5);
    q2 = CreateQueue(5);
    Push(&q1,1);
    Push(&q1,2);
    Push(&q1,3);
    Push(&q1,4);
    Push(&q1,5);
    transferReverse(&q1,&q2);
    printf("%d\n",Pop(&q2));
    printf("%d\n",Pop(&q2));
    printf("%d\n",Pop(&q2));
    printf("%d\n",Pop(&q2));
    printf("%d\n",Pop(&q2));
    return 0;
}