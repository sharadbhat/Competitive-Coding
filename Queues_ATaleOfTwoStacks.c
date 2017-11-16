// HACKERRANK
// https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

struct NODE
{
    int val;
    struct NODE *next;
};

typedef struct NODE node;

node *head = NULL;

int main()
{
    int tries, i;
    scanf("%d", &tries);
    node *present = NULL;
    for(i = 0; i < tries; i++)
    {
        int in1, in2;
        scanf("%d", &in1);
        if(in1 == 1)
        {
            scanf("%d", &in2);
            node *newnode = (node *)malloc(sizeof(node));
            newnode->val = in2;
            if(head == NULL)
            {
                head = newnode;
                present = head;
            }
            else
            {
                present->next = newnode;
                present = newnode;
            }
            newnode->next = NULL;
        }
        else if(in1 == 2)
        {
            node *temp = head;
            head = head->next;
            free(temp);
            temp = NULL;
        }
        else if(in1 == 3)
        {
            printf("%d\n", head->val);
        }
    }
}
