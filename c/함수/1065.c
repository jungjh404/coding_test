#include <stdio.h>

int main() {
    int X;
    scanf("%d", &X);

    if (X < 100){
        printf("%d\n", X);
        return 0;
    }

    int cnt = 99;

    for (int i = 100; i <= X; i++){
        int a = i / 100;
        int b = (i % 100) / 10;
        int c = i % 10;

        if (2*b == a + c) {
            cnt++;
        }
    }

    printf("%d\n", cnt);
}