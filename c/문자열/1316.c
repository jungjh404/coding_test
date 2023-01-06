#include <stdio.h>
#include <string.h>


int main() {
    int N;
    scanf("%d", &N);
    
    int answer = 0;

    for (int i=0; i<N; i++){
        int arr[26] = {0};
        
        char s[101];

        scanf("%s", s);

        char prev_c;
        for (int j=0; j<strlen(s); j++){
            if(j==0){
                prev_c = s[j];
                arr[s[j]-97] = 1;
            }
            else{
                if (prev_c != s[j]){
                    if (arr[s[j]-97] == 1) {
                        answer += 1;
                        break;
                    }
                    arr[s[j]-97] = 1;
                    prev_c = s[j];
                }
            }
        }
    }
    printf("%d\n", N-answer);
}