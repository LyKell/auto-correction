#include <stdio.h>

void main(int argc, char** argv){
  int a = argv[1];
  int b = argv[2];

  printf("La somme de %ld et %ld vaut %ld\n", b, a, a+b);
  return 3;
}