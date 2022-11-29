#include "queue.h"
#include <stdio.h>

int main(){
    int food,waktu;
    int max_waktu = 0;
    int min_waktu = 999;
    int count_food = 0;
    Queue antrian;
    int count_antrian = 0;
    CreateQueue(&antrian);
    scanf("%d",&food);
    while (food != 0){
        if (food==1){
            scanf("%d",&waktu);
            if (waktu > 0){
                enqueue(&antrian,food);
                enqueue(&antrian,waktu);
                count_antrian +=1;
                }
            }

        else if (food == 2){
            if (count_antrian>0){
                dequeue(&antrian,&food);
                count_food +=1;
                dequeue(&antrian,&waktu);
                if (waktu > max_waktu){
                    max_waktu = waktu;
                }
                if (waktu < min_waktu){
                    min_waktu = waktu;
                }
                count_antrian -=1;
            }
        }
        scanf("%d",&food); 
    }

    if (count_food == 0){
        min_waktu = 0;
        printf("%d\n",count_food);
        printf("%d\n",min_waktu);
        printf("%d\n",max_waktu);
    }
    else{
        printf("%d\n",count_food);
        printf("%d\n",min_waktu);
        printf("%d\n",max_waktu);
    }
    return 0;
}