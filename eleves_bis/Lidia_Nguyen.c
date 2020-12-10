#include <stdio.h>
#include <stdlib.h>

int main(){
  int a = atoi(argv[1]);
  int b = atoi(argv[2]);

  printf("La somme de %ld et %ld vaut %ld\n", b, a, a+b);
  return 0;
}