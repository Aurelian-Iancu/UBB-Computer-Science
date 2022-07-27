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
b db 01011010b
a dw 1001101110111110b
c db 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; Sa se inlocuiasca bitii 0-3 ai octetului B cu bitii 8-11 ai cuvantului A
    ; c = 01011011 = 91
    
    mov bl, 0
    mov ax, 0
    mov cl, 0
    
    mov bl, [b] ; bl = 01011010
    mov bh, 0; bx = 0000000001011010
    mov ax, [a] ; ax = 1001101110111110
    
    and bl, 11110000b ; bits 0-3 of b now have the value 0
    
    and ax, 0000111100000000b ; bits 8-11 of a are now isolated
    mov cl, 8
    ror ax, cl ; rotate 8 times to the right
    or bx, ax ; bx = 0000000001011011 = 91
    
    mov [b], bl ; c = 01011011 = 91
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
