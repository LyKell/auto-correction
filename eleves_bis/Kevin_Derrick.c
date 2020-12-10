#include <stdio.h> /* Pour printf */
#include <stdlib.h> /* Pour atoi */

int main(int argc, char* argv[]){
  /* Conversion des arguments en entiers */
  int a = atoi(argv[1]);
  int b = atoi(argv[2]);

  printf("La somme de %d et %d vaut %d\n", a, b, a+b);
  return 0;
}