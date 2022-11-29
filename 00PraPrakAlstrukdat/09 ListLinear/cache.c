 #include<stdio.h>
 #include "listlinier.h"
 
 int main(){
	int n ,q, number;
	scanf("%d", &n);
	scanf("%d", &q);
	List cache;
	CreateEmpty(&cache);
	address P, P1;
	
	for(int i=1; i <= n; i++){
		P  = Alokasi(i);
		InsertLast(&cache, P);
	}
	
	for(int i =0 ; i < q; i++){
		scanf("%d", &number);
		address angka;
		angka = Search(cache, number);
		if (angka != Nil){
			DelP(&cache, number);
			InsVFirst(&cache, number);
			printf("hit ");
			PrintInfo(cache);
			printf("\n");
		}
		else {
			DelLast(&cache, &P1);
			P = Alokasi(number);
			InsertFirst(&cache, P);
			printf("miss ");
			PrintInfo(cache);
			printf("\n");
		}
	}
	return 0;
}
