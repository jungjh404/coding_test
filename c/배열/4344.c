#include <stdio.h>
#include <stdlib.h>

int main() {
    int c;
    scanf("%d", &c);

    for (int i = 0; i < c; i++){
        int N;
        scanf("%d", &N);

        int *arr = (int *) malloc(sizeof(int) * N);
        float avg = 0;

        for (int j=0; j < N; j++){
            scanf("%d", &arr[j]);
            avg += arr[j];
        }

        avg = avg / N;

        int cnt = 0;

        for (int j = 0; j < N; j++){
            if (arr[j] > avg){
                cnt += 1;
            }
        }
        
        float answer = (float) cnt / N * 100;
        printf("%.3f%%\n", answer);
    }
}