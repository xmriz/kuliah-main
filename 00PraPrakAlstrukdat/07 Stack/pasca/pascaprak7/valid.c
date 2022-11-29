#include "valid.h"

Stack validParantheses(char* input, int length){
    Stack S;
    CreateEmpty(&S);
    int i = 0;
    char a;
    while(i<length){
        if((input[i]=='(')||(input[i]=='[')||(input[i]=='{')){
            a = input[i];
        }
        else{
            if((a =='(') && (input[i] == ')')){
                Push(&S,a);
                Push(&S,input[i]);
            }
            if((a =='{') && (input[i] == '}')){
                Push(&S,a);
                Push(&S,input[i]);
            }
            if((a =='[') && (input[i] == ']')){
                Push(&S,a);
                Push(&S,input[i]);
            }
        }
        i++;
    }
    return S;
}
/* Proses: Memasukkan parantheses (dari input) yang valid secara berurutan ke dalam Stack */
/* I.S. input adalah string, yang berisi parantheses baik secara acak maupun teratur, dan panjang dari string */
/* Contoh input dan hasil parantheses yang valid:
    1. () 2 -> ()
    2. []) 3 -> []
    3. {[} 3 -> --kosong--
    4. ()[]{} 6 -> ()[]{}
*/