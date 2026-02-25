#include <stdio.h>

int main() {
    int a, b, sum, product;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    sum = a + b;
    product = a * b;

    printf("Sum = %d\n", sum);
    printf("Product = %d\n", product);

    return 0;
}
