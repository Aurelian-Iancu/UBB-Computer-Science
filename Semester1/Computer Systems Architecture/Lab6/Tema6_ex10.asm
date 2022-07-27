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
a dw 1234h,1A2Bh,1E98h
len equ ($-a)/2 ; lenght of word string
b1 db 0
b2 db 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, a; is esi we keep the offset of string a
        cld ; df=0, the string is parsed from left to right
        mov ecx, len ; we'll have len steps for the loop
        mov ebx, 0 ; index for first string
        mov edx, len - 1; index for second string
    
        repeta: 
            lodsb ; high byte in al
            mov [b1+ebx],al
            lodsb ; low byte in al
            mov [b2+edx],al
            inc ebx
            inc edx
        loop repeta
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
        
        