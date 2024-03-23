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
        mov bx,0
        or bx, 11110000000000000000000000000000; punem 1 pe bitii 0-3
        mov ax,[a]; izolam bitii 0-3 ai lui a
        and ax, 0000000000001111b;
        mov cl,8;
        rol ax,cl; rotim 8 pozitii spre stanga
        or bx,ax ; punem bitii in rezultat
        and bx, 11111111000000111111111111111111; punem 0 pe bitii 8-13 
        mov ax,0; izolam bitii 4-13 ai lui a
        and ax,0011111111110000;
        mov cl,10
        ror ax,cl,10; rotim spre dreapta 10 pozitii
        or bx,ax
        
        
    
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
