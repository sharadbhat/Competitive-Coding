// HACKERRANK
//

#include <math.h>
#include <stdio.h>
#include <string.h>

int main()
{
    int diff, i;
    int aar[26] = {0};
    int bar[26] = {0};
    char a[10000];
    char b[10000];
    scanf("%s", a);
    scanf("%s", b);
    for(i = 0; a[i] != '\0'; i++)
    {
        aar[(int)(a[i] - 'a')] += 1;
    }
    for(i = 0; b[i] != '\0'; i++)
    {
        bar[(int)(b[i] - 'a')] += 1;
    }
    for(i = 0; i < 26; i++)
    {
        diff += fabs(aar[i] - bar[i]);
    }
    printf("%d", diff);
}s
