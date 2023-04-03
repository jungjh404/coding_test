#include <stdio.h>
#include <string.h>

int main(){
    int T;
    scanf("%d", &T);

    for(int t=1; t<T+1; t++){
        char s[100002];
        char x, y;
        scanf("%s %c %c", s, &x, &y);
        
        int len = strlen(s);

        char answer[len+1];
        memset(answer, '0', sizeof(char)*len);
        answer[len] = '\0';

        int flag = 0;

        for (int i=0; i<len; i++){
            if (y <= s[i]){

            }
            else if (x <= s[i]){
                
            }
        }

        printf("%s\n", answer);
    }
}