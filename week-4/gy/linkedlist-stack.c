#include <stdio.h>
#include <stdlib.h>
void push (int);
int pop ();
void print_s ();
typedef struct node{
 int data;
 struct node* next;
}stack;

stack *top = NULL; // 맨 앞에서 가만히 있는다.

int main () { 
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);
    print_s();
    pop();
    pop();
    print_s();

    return 1;
}

void push (int data) {
    stack* pNode = (stack*)malloc(sizeof(stack)); // 동적 할당
    pNode->data = data;
    if (top == NULL){ // top이 비어 있으면
        top = pNode; // 그 자체
    }else{
        pNode->next = top; // next는 그 전에꺼
        top = pNode; // top 갱신
    }
}
int pop(){
    int result;
    stack* pNode = (stack*)malloc(sizeof(stack));
    if (top == NULL){
        return 0;
    }
    pNode = top; // pop할 노드
    top = pNode->next; // pop할 노드 next로 갱신
    result = pNode->data;
    free(pNode); // pop
    return result;
}

void print_s () {
    stack* down = top;
    while (down != NULL){
        printf("%d\n",down->data);
        down = down->next; // 전꺼 포인팅
    }
    printf("\n");
}