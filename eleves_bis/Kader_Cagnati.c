#include <stdio.h>
#include <stdlib.h>

int main(){
  int a = atoi(argv[1]);
  int b = atoi(argv[2]);

  printf("La somme de %d et %d vaut %d\n", a, b, a+b);
  return 0;
}