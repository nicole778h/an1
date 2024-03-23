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
a db 10101010b 
b db 11001100b
c db 00110011b
d db 01010101b
;de aici octetii 4-6 sunt 010,100,011,101
; our code starts here
segment code use32 class=code
    start:
        ; ...
    mov ax,0; calculam rezultatul in ax
    mov bl,[a];bl=10101010b
    and bl,01110000b; izolam bitii 4-6 ai lui a
    mov cl,4
    ror bl,cl; rotim la dreapta cu 4 pozitii
    mov bh,0; conversie byte to word
    add ax,bx; 00000111b
    
    mov bl,[b]; bl =11001100b
    and bl,01110000b; izolam bitii 4-6 ai lui b
    mov cl,4
    ror bl,cl; rotim la dreapta cu 4 pozitii
    mov bh,0
    add ax,bx
    
    mov bl,[c]; bl=c
    and bl,01110000bl izolam bitii 4-6
    mov cl,4
    ror bl,cl; rotim la dreapta cu 4 pozitii
    mov bh,0
    add ax,bx
    
    mov bl,[d]; bl=d
    and bl,01110000b
    mov cl,4
    ror bl,cl
    mov bh,0
    add ax,bx
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program