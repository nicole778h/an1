bits 32 

global start        


extern exit, fread, fopen, fclose, printf
import exit msvcrt.dll    
import fread msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data
    nume_fisier db "Numere.txt", 0
    mod_acces db "r", 0
    descriptor dd -1
    contor dd 0
    lungime equ 100
    sir times lungime db 0
    format db "Exista %d cifre impare"
    
;Se da un fisier text, Sa se citeasca continutul fisierului, sa se contorizeze numarul de cifre impare si sa se afiseze aceasta valoare (Numele fisierului text este definit in segmentul de date)
segment code use32 class=code
    start:
        ;fopen(nume_fisier, mod_acces)
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4*2
        mov [descriptor], eax
        
        ; Verificam daca deschiderea fisierului a fost executata cu succes
        cmp eax, 0
        je Sfarsit
        
        ;fread(string, size, lungime, file)
        push dword [descriptor]
        push lungime
        push dword 1
        push sir
        call [fread]
        add esp, 4*4
        
        push eax
        
        ;fclose(fisier)
        push dword[descriptor]
        call [fclose]
        add esp, 4*1
        
        pop eax
        
        ;Parcurgem sirul si incrementam contorul
        mov ecx, eax
        jecxz Sfarsit
        cld
        mov esi, sir
        
        Repeta:
            lodsb
            ;  Verificam daca e cifra:
            cmp al, '0'
            jb nu_e_cifra
            cmp al, '9'
            jg nu_e_cifra
            
            ; Verificam paritatea:
            sub al, '0'
            test al, 0000_0001b
            jz  e_par
            inc dword[contor]
            
            nu_e_cifra:
            e_par:
        loop Repeta
        
        ;printf(format, contor)
        push dword [contor]
        push dword format
        call [printf]
        add esp, 4*2
        
        Sfarsit:
        push    dword 0      
        call    [exit]