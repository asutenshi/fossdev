#include <stdio.h>
#include <time.h>

int main(void) {
  time_t now = time(NULL);
  printf("This is C app\n");
  printf("Run time: %ld\n", now);
  return 0;
}