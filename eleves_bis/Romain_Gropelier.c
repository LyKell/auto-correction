#include <stdio.h>
#include <stdlib.h>

void main(int argc, char** argv){
  int a = argv[0];
  int b = argv[1];

  printf("La somme de %ld et %ld vaut %ld\n", b, a, a+b);
  return 0;
}