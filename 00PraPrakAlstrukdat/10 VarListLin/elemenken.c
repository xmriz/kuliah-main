#include <stdio.h>
#include "listsirkuler.h"

int ElemenKeN(List L, int r) {
  address P = First(L);
  int i = 0;
  while (i < r) {
    P = Next(P);
    i++;
  }
  return Info(P);
}

int main () {
  List L;
  int r;
  CreateEmpty(&L);
  int x = -1;
  while (x != 0) {
    scanf("%d", &x);
    if (x != 0) {
      InsVLast(&L, x);
    }
  }
  scanf("%d", &r);
  if (IsEmpty(L)){
    printf("List Kosong\n");
  } else {
    printf("%d\n", ElemenKeN(L, r));
  }
  return 0;
}