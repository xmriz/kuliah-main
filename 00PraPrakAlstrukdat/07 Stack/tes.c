#include <stdio.h>
#include <string.h>

int main(){
    char x[100];
    gets(x);
	int i = 0;
	for (i;i<strlen(x);i++){
		if (x[i] == '('){
			i++;
			if (x[i] == ')'){
				printf("%c", x[i-1]);
				printf("%c", x[i]);
				continue;
				}
			i--;
			continue;
			}
		if (x[i] == '{'){
			i++;
			if (x[i] == '}'){
				printf("%c", x[i-1]);
				printf("%c", x[i]);
				continue;
				}
			i--;
			continue;
			}
		if (x[i] == '['){
			i++;
			if (x[i] == ']'){
				printf("%c", x[i-1]);
				printf("%c", x[i]);
				continue;
				}
				i--;
			continue;
			}	
		}
	return 0;
	}
