bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
a db 01;
b dw 8;
c db 03;
d dd 04;
x dq 12;

a1 dd 2;
a2 dd 7;
a3 dd 6;
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;d-(7-a*b+c)/a-6+x/2 unsigned representation 4-(7-1*8+3)/1 -6 +12/2
        mov Al, 0;
        mov Al, [a]; Al = a;
        mov Ah, 0; AX = a;
        mul word[b]; DX:AX = a*b;
        push DX;
        push AX;
        pop EAX; EAX = a*b;
        mov EDX,0;
        mov EDX, [a2]; EDX = 7
        sub EDX,EAX; EDX = 7-a*b
        mov EBX, EDX; EBX = 7-a*b;
        mov EDX, 0; EDX = 0;
        mov Al, 0;
        mov Al, [c]; Al = c;
        mov Ah, 0; AX = c;
        mov DX, 0; DX:AX = c;
        push DX;
        push AX;
        pop EAX; EAX = c;
        add EBX, EAX; EBX = 7-a*b+c
        mov Al, 0;
        mov Al, [a]; Al = a;
        mov Ah, 0; AX = a;
        mov CX, AX; CX = a;
        mov EAX, 0;
        mov EAX, EBX; EAX = 7- a*b +c;
        push EAX;
        pop AX; 
        pop DX; DX:AX = 7- a*b +c
        div CX; AX = cat(7- a*b +c)/a, DX = rest(7- a*b +c)/a;
        mov EBX, 0;
        mov EBX, [d]; EBX = d;
        mov DX, 0; DX:AX = (7- a*b +c)/a
        push DX;
        push AX;    
        pop EAX; EAX = (7- a*b +c)/a
        sub EBX, EAX; EBX = d - (7- a*b +c)/a
        sub EBX, [a3]; EBX = d - (7- a*b +c)/a - 6
        mov EAX, 0;
        mov EDX, 0;
        mov EAX, [x];
        mov EDX, [x+4]; EDX:EAX = x 
        div dword[a1]; EAX = cat(x/2), EDX = rest(x/2)
        add EBX, EAX; EBX = d-(7-a*b+c)/a-6+x/2
        
        
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
