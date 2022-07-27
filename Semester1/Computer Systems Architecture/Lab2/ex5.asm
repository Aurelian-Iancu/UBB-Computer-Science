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
a db 100;
b db 200;
c db 100;
d dw 05;

a1 db 20;
a2 db 10;
a3 dw 3;
a4 dw 5;
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;3*[20*(b-a+2)-10*c]/5
        mov AX, 0; AX = 0
        add Al, [b]; Al = b
        sub Al, [a]; Al = b-a
        add Al, 2; Al = b-a+2
        mul byte[a1]; AX = 20*(b-a+2)
        mov BX,AX; BX = 20*(b-a+2)
        mov EAX,0; EAX = 0
        mov Al,[c]; Al = c;
        mul byte[a2]; AX = 10* c
        sub BX,AX; BX = 20*(b-a+2), AX = 10*c, BX- AX => BX = 20*(b-a+2)-10*c
        mov AX,BX; AX = 20*(b-a+2)-10*c
        mul word[a3]; EAX = 3*[20*(b-a+2)-10*c]
        push DX;
        push AX;
        pop EAX;
        div word[a4]; AX = 3*[20*(b-a+2)-10*c]/5      
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
