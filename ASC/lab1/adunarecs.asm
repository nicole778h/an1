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
    a db 10
    b dw 15
    c dd 20
    d dq 30

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ax,[c]; ax=20
        cdq
        mov bx,[d]; bx=30
        add ax,bx; ax=20+30=50
        mov cl,[a];cl=10
        cbw
        cdq
        sub ax,cx; ax=50-10=40
        mov bx,ax ;bx=40
        mov ax,[c];ax=20
        cdq
        mov cx,[d];cx=30
        sub cx,ax ;cx=30-20=10
        sub bx,cx;bx=40-10=30
        mov ax,[b];ax=15
        cwd
        cdq
        sub bx,ax;bx=30-15=15
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
