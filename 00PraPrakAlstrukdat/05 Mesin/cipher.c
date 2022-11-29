#include <stdio.h>

int main(){
	char x[100];
	gets(x);
	int n;
	n=0;
	int i = 0;
	while(x[i] == ' '){
		i++;
	}
	while (x[i] != ' '){
		n += 1;
		i++;
		if (x[i] == ' '){
			break;
			}
		}
	int j = -1;
	while (x[j+1] != '.'){
		j++;
		if (x[j] == ' '){
			printf("%c", x[j]);
			}
		else {
			if (x[j]+n > 90){
				printf("%c", x[j]+n-26);
			} else {
				printf("%c", x[j]+n);
			}
		}
		if (x[j] == '.'){
			break;
			}
		}
	printf(".\n");
	return 0;
	}
