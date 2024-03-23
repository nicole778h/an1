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
    S db 'a', 'A', 'b', 'B', '2', '%', 'x'
    len equ $-S
    d times len db 0


; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx,len ; punem in ecx lungimea lui s
        mov esi,0; index ul nostru
        mov edi,0; index pentru sir pentru a pune in ordine
        jecxz final; daca ecx este 0 sarim la final
        repeta:
        mov al,[S+esi]; punem in al elementele pe rand
        mov bl, 'a'; in bl punem codul ascii a lui a
        cmp al,bl 
        jae da; daca al>bl inseamna ca caracterul din al este litera mica si sarim la 'da'
        jmp next ; daca al<bl inseamna ca caracterul e litera mare si sarim la 'next' pentru a trece  la elem urm
        da:
        mov [d+edi], al ; punem in d pe al
        inc edi 
        next:
        inc esi ; incrementam esi pentru a trece la urm elem
        loop repeta
        final:
        
        
        
      
        
        
    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
