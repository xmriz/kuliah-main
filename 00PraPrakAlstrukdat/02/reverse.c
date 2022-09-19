#include <stdio.h>
#include <string.h>


int main(){
	char x[100];
	scanf("%s", x);
	int n = strlen(x);
	int i;
	for (i=0;i<n;i++){
		int idx = n-1-i;
		printf("%c",x[idx]);
		}
	printf("\n");
	return 0;
}
