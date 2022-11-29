#include <stdio.h>
#include "garis.h"

void MakeGARIS(POINT P1, POINT P2, GARIS *L){
	PAwal(*L) = P1;
	PAkhir(*L) = P2;
	}	

void BacaGARIS(GARIS *L){
	float a,b,c,d;
	POINT P1, P2;
	scanf("%f %f", &a, &b);
	P1 = MakePOINT(a,b);
	scanf("%f %f", &c, &d);
	P2 = MakePOINT(c,d);
	while (a == b && c==d){
		printf("Garis tidak valid\n");
		scanf("%f %f", &c, &d);
		P2 = MakePOINT(c,d);
		}
	MakeGARIS(P1, P2, * L);
	}
	
void TulisGARIS(GARIS L){
	printf("((%f,%f),(%f,%f))", Absis(PAwal(L)), Ordinat(PAwal(L)), Absis(PAkhir(L)), Ordinat(PAkhir(L)));
	}

float PanjangGARIS(GARIS L){
	return (Panjang(PAwal(L), PAkhir(L)));
	}

float Gradien(GARIS L){
	float m;
	m = (Ordinat(PAkhir(L)) - Ordinat(PAwal(L))) / (Absis(PAkhir(L)) - Absis(PAwal(L)));
	return m;
	}
	
boolean IsTegakLurus(GARIS L1, GARIS L2){
	return (Gradien(L1)*Gradien(L2) == (-1));
	}
	
boolean IsSejajar(GARIS L1, GARIS L2){
	return (Gradien(L1) == Gradien(L2));
	}
