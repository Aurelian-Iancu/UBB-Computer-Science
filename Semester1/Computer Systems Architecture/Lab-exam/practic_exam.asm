bits 32

global start


extern exit, fopen, fread, fclose, printf           
import exit msvcrt.dll  
import fopen msvcrt.dll 
import fread msvcrt.dll 
import fclose msvcrt.dll 
import printf msvcrt.dll


segment data use32 class=data
file db "file.txt", 0
acces_mode db "r", 0
descriptor dd -1

msg db "nr of voc: ", 0    
msg1 db "  text: ", 0                         
len equ 100             
number_voc dd 0                
text times 100 db 0
format db "%d", 0
vocale resb 100
char_format db "%c", 0


segment code use32 class=code
start:
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    
    push dword acces_mode
    push dword file
    call [fopen]
    add esp, 4*2

    mov [descriptor], eax
    cmp eax, 0
    je .final

    push dword [descriptor]
    push dword len
    push dword 1
    push dword text
    call [fread]
    add esp, 4*4

    mov ecx, eax
    mov esi, text
    mov edi, vocale
                                              
    .loop:
    mov al, [esi]
    cmp al, '!'
    je .final

    cmp al, 'a'
    je .good
    cmp al, 'e'
    je .good
    cmp al, 'i'
    je .good
    cmp al, 'o'
    je .good
    cmp al, 'u'
    je .good
    cmp al, 'A'
    je .good
    cmp al, 'E'
    je .good
    cmp al, 'I'
    je .good
    cmp al, 'O'
    je .good
    cmp al, 'U'
    je .good

    cmp al, 'z'
    jg .not_consone

    cmp al, 'A'
    jb .not_consone

    cmp al, 'a'
    ja .next

    cmp al, 'Z'
    jb .next
                                                  
    jmp .not_consone

    jmp .next

    .good:
    inc byte[number_voc]
    mov byte [edi], al
    inc edi
    jmp .next

    .not_consone:
    mov byte [edi], al
    inc edi
                                            
    .next:
    inc esi
    loop .loop
                                        
    .final:
    push dword msg
    call[printf]
    add esp, 4

    push dword [number_voc]
    push dword format
    call [printf]
    add esp, 4*2

    push dword msg1
    call[printf]
    add esp, 4

    mov esi, vocale
    mov ecx, [number_voc]
                                             
    .loop_2:
    push ecx
    mov ebx, 0
    mov bl, [esi]
    inc esi

    push dword ebx
    push dword char_format
    call [printf]
    add esp, 4*2
                                               
    pop ecx
    loop .loop_2
                                                  
    push dword[descriptor]
    call [fclose]
    add esp, 4*1

    push    dword 0      
    call    [exit]
