#include <stdio.h>
#include <stdlib.h>
#include "removeDuplicate.h"


List removeDuplicate(List l){
	List lout;
	CreateEmpty(&lout);
	address P = First(l);
	address s;
    while(P != Nil){
		s = Search(lout, Info(P));
		if (s == Nil) {
			InsertLast(&lout, Alokasi(Info(P)));
			}
        P = Next(P);
		}
	return lout;	
	}

/*
    Diberikan sebuah list linier yang sudah terurut membesar,
    kembalikan list baru yang elementnya unik
    Contoh input/output:
    input:  [1,1,2,2,3,4,5,6,6,7]
    output: [1,2,3,4,5,6,7]

    input:  [1,1,1,1,1,1]
    output: [1]
*/
