#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv){
  int a = atoi(argv[1]);
  int b = atoi(argv[2]);

  printf("La somme de %d et %d vaut %d\n", b, a, a+b);
  return 0;
}