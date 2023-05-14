#include<stdio.h>
#include<string.h>

int main () {
  int b = -1;
  char c[16];

  gets(&c);

  if (b == 0xdeadf00d) {
    printf("You win\n");
  } else {
    printf("You lose!\n");
    printf("b = %d\n", b);
  }
}
