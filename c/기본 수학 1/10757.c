#include <stdio.h>
#include <string.h>

int main(){
    char a[10001];
    char b[10001];

    scanf("%s", a);
    scanf("%s", b);

    int len;
    if (strlen(a) > strlen(b)) len = strlen(a);
    else len = strlen(b);

    char new_a[10001];
    char new_b[10001];
    
    for(int i = 0; i < 10001; i++){
        new_a[i] = '0';
        new_b[i] = '0';
    }
    
    new_a[10000 - strlen(a)] = '\0';
    new_b[10000 - strlen(b)] = '\0';
    
    strcat(new_a, a);
    strcat(new_b, b);

    char answer[10002];
    for(int i = 0; i < 10002; i++){
        answer[i] = '0';
    }

    answer[10001] = '\0';

    int buffer = 0;
    for (int i = 9999; i >= 0; i--){
        int sum = (new_a[i]-'0') + (new_b[i]-'0') + buffer;

        if (sum >= 10) buffer = 1;
        else buffer = 0;
        
        answer[i+1] = (char) ((sum % 10) + 48);
    }
    if (buffer == 1) answer[0] = '1';
    
    int flag = 0;

    for (int i=0; i<10001; i++){
        if (flag == 0 && answer[i] != '0'){
            flag = 1;
        }

        if (flag == 1){
            printf("%c", answer[i]);
        }
    }
    printf("\n");
}