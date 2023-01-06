#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    int divider = 2;

    while (N != 1){
        if (N % divider == 0){
            printf("%d\n", divider);
            N /= divider;
        }
        else{
            divider += 1;
        }
    }
}