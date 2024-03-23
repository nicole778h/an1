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
    
    ;(50-b-c)*2+a*a+d
    a db 4
    b db 3
    c db 7
    d dw 5

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al,[b]
        mov bl,50
        sub bl,al 
        mov cl,[c]
        sub bl,cl
        mov al,bl
        mov bl,2
        mul bl
        mov cl,al
        mov al,[a]
        mul byte[a]
        add cl,al
        add cl,[d]
        
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
