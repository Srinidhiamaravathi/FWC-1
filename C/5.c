#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 1};
    int size = 5;

    if(arr[0] == arr[size-1]) {
        printf("First and Last are same\n");
    } else {
        printf("Not same\n");
    }

    return 0;
}
