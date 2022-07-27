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
M dd 01110111010101111001101110111110b
N dd 01110100010111010101001011010001b
P dd 00000000000000000000000000000000b
; our code starts here
segment code use32 class=code
    start:
        ; ...
     ;Se dau 2 dublucuvinte M si N. Sa se obtina dublucuvantul P astfel:
     ;bitii 0-6 din P coincid cu bitii 10-16 a lui M
     ;bitii 7-20 din P concid cu bitii obtinuti 7-20 in urma aplicarii M AND N.
     ;bitii 21-31 din P coincid cu bitii 1-11 a lui N.
    mov ebx, 0 ; the result is going to be in ebx
    mov eax, 0;
    
    mov eax, [M]
    and eax, 00000000000000011111110000000000b ; we isolate the 10-16 bits from M to add in P
    mov cl,10
    ror eax,cl ; rotating 10 bits to the right
    or ebx,eax ; putting the result in ebx
    
    mov eax,[M]
    mov ecx,[N]
    
    and eax,ecx ; result is in eax
    and eax, 00000000000111111111111110000000b ; we isolate bits 7-20 
    or ebx,eax ; putting the result in ebx
    
    mov eax, [N]
    and eax, 00000000000000000000111111111110b ; we isolate bits 1-11
    mov cl, 20
    rol eax,cl ; rotating to the left
    or ebx,eax 
    
    mov [P],ebx ; result is in P
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
