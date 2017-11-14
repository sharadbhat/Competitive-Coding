// HACKERRANK
//

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

struct NODE
{
    char b;
    struct NODE *below;
};

typedef struct NODE node;

node *top = NULL;

int main()
{
    int tries, i;
    char a[1000];
    scanf("%d", &tries);
    for(i = 0; i < tries; i++)
    {
        top = NULL;
        int flag = 0;
        scanf("%s", a);
        int j;
        for(j = 0; a[j] != '\0'; j++)
        {
            if(a[j] == '(' || a[j] == '{' || a[j] == '[')
            {
                node *newnode = (node *)malloc(sizeof(node));
                newnode->b = a[j];
                newnode->below = top;
                top = newnode;
            }
            else
            {
            	if(top == NULL)
            	{
            		flag = 1;
            		break;
				}
            	if(a[j] == ')')
            	{
            		if(top->b != '(')
            		{
            			flag = 1;
            			break;
					}
				}
				else if(a[j] == '}')
				{
					if(top->b != '{')
            		{
            			flag = 1;
            			break;
					}
				}
				else if(a[j] == ']')
				{
					if(top->b != '[')
            		{
            			flag = 1;
            			break;
					}
				}
                if(top->below != NULL)
				{
                    top = top->below;
                }
                else
                {
                    top = NULL;
                }
            }
        }
        if(flag == 0 && top == NULL)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
}
