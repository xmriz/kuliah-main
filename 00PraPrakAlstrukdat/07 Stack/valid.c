#include <stdio.h>
#include <string.h>
#include "stack.h"


Stack validParantheses(char* input, int length){
	Stack s;
	CreateEmpty(&s);
	int i = 0;
	for (i;i<length;i++){
		if (input[i] == '('){
			i++;
			if (input[i] == ')'){
				Push(&s,input[i-1]);
				Push(&s,input[i]);
				continue;
				}
			i--;
			continue;
			}
		if (input[i] == '{'){
			i++;
			if (input[i] == '}'){
				Push(&s,input[i-1]);
				Push(&s,input[i]);
				continue;
				}
			i--;
			continue;
			}
		if (input[i] == '['){
			i++;
			if (input[i] == ']'){
				Push(&s,input[i-1]);
				Push(&s,input[i]);
				continue;
				}
				i--;
			continue;
			}	
		}
	return s;
	}
