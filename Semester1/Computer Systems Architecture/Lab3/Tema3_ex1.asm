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
a db 1;
b dw 2;
c dd 3;
d dq 4;

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;unsigned interpretation
        ;(a+d+d)-c+(b+b)
        mov Al, 0; Al = 0
        mov Al, [a]; Al = a
        mov Ah, 0; AX = a
        mov DX, 0; DX:AX = a
        push DX;
        push AX;
        pop EAX; EAX = a
        mov EDX, 0; EDX:EAX = a 
        mov EBX, 0; EBX = 0
        mov ECX, 0; ECX = 0
        mov EBX, [d];
        mov ECX, [d+4]; ECX:EBX = d
        add EAX, EBX; 
        adc EDX, ECX; EDX:EAX = a + d
        add EAX, EBX; 
        adc EDX, ECX; EDX:EAX = a + d + d
        mov EBX, 0; EBX = 0
        mov EBX, [c]; EBX = c
        mov ECX, 0; ECX: EBX = c
        sub EAX, EBX; 
        sbb EDX, ECX; EDX:EAX = (a + d + d) - c
        mov BX, 0; BX = 0
        mov BX, [b]; BX = b
        mov CX, 0; CX:BX = b
        push CX
        push BX
        pop EBX; EBX = b
        mov ECX, 0; ECX:EBX = b
        add EAX, EBX; 
        adc EDX, ECX; EDX:EAX = (a + d + d) - c + 
        add EAX, EBX; 
        adc EDX, ECX; EDX:EAX = (a + d + d) - c + (b + b)

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
