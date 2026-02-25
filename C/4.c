#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int n;

    printf("Enter string: ");
    scanf("%s", str);

    printf("Enter n: ");
    scanf("%d", &n);

    for(int i = n; i < strlen(str); i++) {
        printf("%c", str[i]);
    }

    return 0;
}
