#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void win() {
  printf("Access granted...\n");
  system("/bin/sh");
}

void dangerous() {
  char buff[21];
  gets(&buff);
}

int main (int argc, char *argv[])
{
  dangerous();
  return 0;
}
