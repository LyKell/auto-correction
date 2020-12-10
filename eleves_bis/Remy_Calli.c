#include <stdio.h>

void main(int argc, char** argv){
  int a = atoi(argv[0]);
  int b = atoi(argv[1]);

  printf("La somme de %ld et %ld vaut %ld\n", b, a, a+b);
  return 3;
}