    // C aja yakk :D
    // Program hanya berlaku untuk angka 1-9 wkwk :v

    #include<stdio.h>
    #include<stdlib.h>
    #include<string.h>

    char stack[50];
    int top=-1;
    void push(char ch)
    {
        stack[++top]=ch;
    }
    char pop()
    {
        return stack[top--];
    }
    void convert(char exp[])
    {
        int l,i,j=0;
        char tmp[20];
        strrev(exp);
        l=strlen(exp);
        for(i=0;i<50;i++){
            stack[i]='\0';
        }
        printf("\nThe Infix Expression is : : ");
        for(i=0;i<l;i++){
            if(exp[i]=='+'||exp[i]=='-'||exp[i]=='*'||exp[i]=='/')
                push(exp[i]);
            else if (exp[i]==' '){
                continue;
            }
            else{
                tmp[j++]=exp[i];
                tmp[j++]=pop();
            }
        }
        tmp[j]=exp[top--];
        strrev(tmp);
        puts(tmp);
    }

    // Main Driver
    int main()
    {
        char exp[50];
        printf("Enter the Postfix Expression : ");
        gets(exp);
        convert(exp);
        return 0;
    }