#include <stdio.h>

int main() {
    int i, j;
    int stars, spaces;
   
    int N;
    scanf("%d", &N);
    if (N % 2 == 0){
        printf("inputan N salah");
    }
    else {
        stars = 1;
        spaces = (N - 1)/2;
        
        /* Iterate through N */
        for(i=1; i<N; i++)
        {
            /* Print spaces */
            for(j=0; j<spaces; j++){
                printf(" ");
            }
            
            /* Print stars */
            for(j=0; j<stars*2; j++){
                printf("*");
            }
            
            /* Move to next line */
            printf("\n");
            
            if(i<((N/2)+1))
            {
                spaces--;
                stars++;
                stars++;
            }
            else
            {
                spaces++;
                stars--;
                stars--;
            }
        }
    }
    
    return 0;
}