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
b db 02;
c db 03;
d db 04;
e dw 05;
f dw 06;
g dw 07;
h dw 08;

a1 db 2;
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;(e+g-2*b)/c
        mov AX, 0; AX = 0
        mov AX, [e]; AX = e
        add AX, [g]; AX = e+g
        mov BX, AX; BX = e+g
        mov AX, 0; AX = 0
        mov Al, [b]; Al = b
        mul byte[a1]; AX = 2*b
        sub BX, AX; BX = e+g-2*b
        mov AX, BX; AX = e+g-2*b
        div byte[c]; AX = (e+g-2*b)/c      
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
