#include <stdio.h>

int main(){
  int a = argv[0];
  int b = argv[1];

  printf("La somme de %ld et %ld vaut %ld\n", b, a, a+b);
  return 3;
}