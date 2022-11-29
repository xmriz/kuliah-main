#include <stdio.h>  
#include <string.h>  
#include <ctype.h>

int main()  
{  
    char str1[100];  // declaration of char array  
    char str2[100];  // declaration of char array  
    int value; // declaration of integer variable  

    scanf("%s",str2); 
    scanf("%s",str1);  

    int i=0;
    for (i;i<100;i++){
        str1[i] = tolower(str1[i]);
        str2[i] = tolower(str2[i]);
    } 

    value = strcmp(str1,str2);  
    if(value == 0){
        printf("Ya\n");  
    } else {
        printf("Tidak\n");
    }

    return 0;  
}  