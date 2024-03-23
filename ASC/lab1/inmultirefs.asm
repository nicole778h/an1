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
     a db 5
    b dd 15
    c db 25
    x dq 10

; our code starts here
segment code use32 class=code
    start:
        ; ...
        movzx eax,byte[a]; eax=a=5
        mul byte[a]; eax=25
        mov ebx,[b]; ebx=b=15
        add eax,ebx; eax=25+15=40
        mov edx,0; edx:eax=40
        
        ;movzx eax,byte[c]; eax=c=25
        mov bl,[c];al=25
        mov bh,0; cbw
        div byte[a]; al=c/a=25/5=5
        add bx,[a]; ax=10
        ;mov bx,ax; bx=10
        movzx eax,ax; cwde
        mov ecx,eax; edx=10
        mov eax, ebx; eax=40
        ;mov ecx,edx;ecx=10
        div ecx
        ;mov ecx,eax
        ;div dx
        ; movzx eax,bx cwde
        
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
