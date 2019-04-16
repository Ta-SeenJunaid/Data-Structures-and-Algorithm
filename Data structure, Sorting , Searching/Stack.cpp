// Bismillahir Rahmanir Raheem
#include <bits/stdc++.h>
using namespace std;

#define stack_max 100

typedef struct{
    int top;
    int data[stack_max];
}Stack;

void push(Stack *s, int item)
{
    if(s->top < stack_max){
        s->data[s->top]=item;
        s->top=s->top+1;
    }
    else{
        printf("Stack is full!\n");
    }
}

int pop(Stack *s)
{
    int item;
    if(s->top == 0){
        printf("Stack is empty!\n");
    }else{
        s->top = s->top-1;
        item = s->data[s->top];
        return item;
    }
}

int main()
{
    Stack my_stack;
    int item;

    my_stack.top =0;
    push(&my_stack,123);
      push(&my_stack,49334);
        push(&my_stack,123);

        item = pop(&my_stack);
        printf("%d\n",item);

         item = pop(&my_stack);
        printf("%d\n",item);


        return 0;
}
