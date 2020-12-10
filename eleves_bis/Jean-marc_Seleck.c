#include <stdlib.h>

void main(int argc, char** argv){
  int a = atoi(argv[1]);
  int b = atoi(argv[2]);

  printf("La somme de %ld et %ld vaut %ld\n", b, a, a+b);
  return 0;
}