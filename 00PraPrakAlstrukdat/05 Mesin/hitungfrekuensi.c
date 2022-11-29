#include <stdio.h>
#include "mesinkarakter.h"

char currentChar;
boolean EOP;
static FILE *pita;
static int retval;

int hitungfrekuensi(){
	int count;
	count = 0;
	START();
	while (!IsEOP()){
		if ((currentChar == 't') || (currentChar == 'T')){
			ADV();
			if ((currentChar == 'i') || (currentChar == 'I')){
				ADV();
				if ((currentChar == 'g') || (currentChar == 'G')){
					ADV();
					if ((currentChar == 'a') || (currentChar == 'A')){
						count += 1;
						ADV();
						} else {ADV(); continue;}
					} else {ADV(); continue;}
				} else {ADV(); continue;}
			} else {ADV(); continue;}
		}
	return count;
	}
	
