#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
  int a = argv[1];
  int b = argv[2];

  printf("La somme de %d et %d vaut %d\n", a, b, a+b);
  return 0;
}