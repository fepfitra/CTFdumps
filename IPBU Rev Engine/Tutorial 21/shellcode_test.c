#include <stdio.h>
#include <unistd.h>

int main() {
  char buffer[64];
  printf("Buffer ada di: %p\n", &buffer);
  fflush(stdout);

  read(0, &buffer, 128);

  return 0;
}
