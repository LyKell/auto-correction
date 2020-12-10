#include <stdio.h> /* Pour printf */
#include <stdlib.h> /* Pour atoi */

int main(int argc, char* argv[]){
  int a = atoi(argv[0]);
  int b = atoi(argv[1]);

  printf("La somme de %d et %d vaut %d\n", a, b, a+b);
  return 0;
}