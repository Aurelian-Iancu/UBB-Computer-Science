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
d dw 05;

a1 db 5;
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;d+[(a+b)*5-(c+c)*5]
        mov ax,0;
        mov al, [a]; al = a
        add al, [b]; al = a+b
        mul byte[a1]; ax = (a+b)*5
        mov bx,ax; bl = (a+b)*5
        mov ax,0; ax = 0
        mov al, [c]; al = c
        add al, [c]; al = c+c
        mul byte[a1]; ax = (c+c)*5
        sub bx,ax; bx = (a+b)*5 - (c+c)*5
        mov ax,bx; ax = (a+b)*5 - (c+c)*5
        add ax, [d]; = d+[(a+b)*5-(c+c)*5]   
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
