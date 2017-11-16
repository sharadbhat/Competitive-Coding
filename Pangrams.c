// HACKERRANK
// https://www.hackerrank.com/challenges/pangrams/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int flag = 0;
    char s[1000] = {0};
    fgets(s, sizeof(s), stdin);
    int i, t[26]={0};
    for(i = 0; s[i] != 0; i++)
    {
        if(((int)(s[i]) >= 97) && ((int)(s[i]) <= 122))
            t[(int)(fabs(97 - (int)(s[i])))] = 1;
        else if(((int)(s[i]) >= 65) && ((int)(s[i]) <= 90))
            t[(int)(fabs(65 - (int)(s[i])))] = 1;
    }
    for(i = 0; i < 26; i++)
        if(t[i] == 0)
        {
            flag = 1;
            break;
        }
    if(flag == 1)
        printf("not pangram");
    else
        printf("pangram");
}
