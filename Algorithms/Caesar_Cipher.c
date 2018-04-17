// HACKERRANK
// https://www.hackerrank.com/challenges/caesar-cipher-1/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    char arr[101];
    int i, k, n, x, rem;
    scanf("%d", &k);
    scanf("%s", arr);
    scanf("%d", &n);
    for(i = 0;i < k; i++)
    {
        x = (int)arr[i];
        rem = n % 26;
        if(x >= 65 && x <= 90)            //upper case
        {
            if(x <= (90 - rem))
                printf("%c", (arr[i] + rem));
            else
            {
                int v = 90 - x;
                printf("%c", (rem-v+64));
            }
        }
        else if(x >= 97 && x <= 122)      //lower case
        {
            if(x <= (122 - rem))
                printf("%c", (arr[i] + rem));
            else
            {
                int v = 122 - x;
                printf("%c", (rem - v + 96));
            }
        }
        else
            printf("%c", arr[i]);
    }
}
