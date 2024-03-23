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
    a dw 0111011101010111b
    b db 01101101b

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ebx,0
        or ebx, 00000000000000000000000000001111b; punem 1 pe bitii 0-3
        mov ax,[a]; izolam bitii 0-3 ai lui a
        movzx eax,ax;
        and eax,00000000000000000000000000001111b ;
        mov cl,4;
        rol eax,cl; rotim 4 pozitii spre stanga
        or ebx,eax ; punem bitii in rezultat
        and ebx, 11111111111111111100000011111111b; punem 0 pe bitii 8-13 
        mov eax,[a]; izolam bitii 4-13 ai lui a
        and eax,00000000000000000011111111110000b;
        mov cl,10
        rol eax,cl; rotim spre stanga 10 pozitii
        or ebx,eax
        mov al,[b]
        movzx eax,al; conversie byte do de
        ;mov eax,[b]; izolam bitii 2-7 ai lui b
        and eax, 00000000000000000000000011111100b
        mov cl,22
        rol eax,cl; rotim 22 poz spre stanga
        or ebx,eax
        or ebx, 11000000000000000000000000000000b
        
    
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
