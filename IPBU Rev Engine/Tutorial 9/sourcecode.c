#include<stdio.h>

int p = 100;
int testing = 0;

int jumlah(int a, int b) {
  int c = a + b;
  return c;
}

int main (int argc, char *argv[])
{
  printf("Hello World\n");
  int x = 10;
  int y = 20;
  int z = jumlah(x, y);

  printf("%d\n", z);

  testing = 1337;
  printf("%d\n", testing);
  return 0;
}
