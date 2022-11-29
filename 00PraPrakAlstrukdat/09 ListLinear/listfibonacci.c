#include <stdio.h>
#include "listlinier.h"

int main() {
    List fibonacci;
    CreateEmpty(&fibonacci);

    infotype el;
    scanf("%d", &el);

    if (el == 0) {
        PrintInfo(fibonacci);
        return 0;
        
    } else if (el == 1) {
		int x;
        scanf("%d", &x);
        InsertLast(&fibonacci, Alokasi(x));
        PrintInfo(fibonacci);
        return 0;
        
    } else {
		int y;
		int z;
		int count = 2;
        scanf("%d", &y);
        scanf("%d", &z);
        InsertLast(&fibonacci, Alokasi(y));
        InsertLast(&fibonacci, Alokasi(z));
        address p1 = First(fibonacci);
        address p2 = Next(p1);
        while (count < el){	
			InsertLast(&fibonacci, Alokasi(Info(p1) + Info(p2)));
			count++;	
			p1 = Next(p1);
			p2 = Next(p1);
				
			}

        
        PrintInfo(fibonacci);
    }

    return 0;
}
