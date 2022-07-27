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
    s1 db 'a', 'b', 'c', 'd', 'e','f';
    l1 equ $ - s1;
    s2 db 'e', 'f', 'g', '1', '2';
    l2 equ $ - s2;
    d times l1 + l2 db 0;
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, l2; ECX = length of s2
        mov esi, l2-1; in ESI we have the last position of s2
        mov ebx, 0; in EBX we have the position in d
        jecxz endFor1
        repeat1:; in this loop we decrease the position in s2 by 1 completing d with the elements form s2
            mov Al, [s2+esi]
            mov [d+ebx], Al
            inc ebx
            dec esi
        loop repeat1       
        endFor1:

        mov ecx, l1/2; ECX = length of s1 / 2 because we take only the even numbers
        mov esi, 1;in ESI we have the first even position which is 1 because we start the index from 0
        jecxz endFor2
        repeat2:; in this loop we increase the position in s1 by 2 completing d with the elements from s1
            mov Al, [s1+esi]
            mov [d+ebx], Al
            add esi, 2
            inc ebx
        loop repeat2
        
        endFor2:
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
