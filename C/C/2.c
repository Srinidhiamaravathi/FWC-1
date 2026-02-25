#include <stdio.h>

int main() {
    int previous = 0;

    for(int i = 0; i <= 10; i++) {
        printf("Current: %d Previous: %d Sum: %d\n", i, previous, i + previous);
        previous = i;
    }

    return 0;
}
