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
    s1 db  1, 3, 6, 2, 3, 7
    s2 db  6, 3, 8, 1, 2, 5
    len equ ($-s1)/2; lungimea celor 2 siruri este egala
    d times len db 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, len; punem in ecx lungimea sirului pentru a face bucla
        mov esi, 0; index ul nostru
        jecxz final; daca ecx este 0 inseamna ca nu avem elemente in sir si trece la final
        repeta:
        mov al,[s1+esi]; punem in al primul element al lui s1
        mov bl,[s2+esi]; punem in al primul element al lui s2
        cmp al,bl ; cmp va face diferenta al-bl
        jae next; daca al>=bl va trece la next
        mov [d+esi], bl; daca al<bl va pune ah in sir
        jmp nu; acest jmp este pus pentru a nu efectua instructiunea de la next daca s-a pus in d deja bl
        next:
        mov [d+esi], al; next pune in d pe al
        nu:
        inc esi ; incrementam esi pentru a continua bucla 
        loop repeta; bucla se repeta pana la valoarea continuta in ecx 
        final:
           
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
