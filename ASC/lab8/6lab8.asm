bits 32 

global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fread, printf
import exit msvcrt.dll 
import fopen msvcrt.dll 
import fread msvcrt.dll 
import fclose msvcrt.dll 
import printf msvcrt.dll 
; our data is declared here 
;Se da un fisier text. Sa se citeasca continutul fisierului, sa se determine cifra cu cea mai mare frecventa si sa se afiseze acea cifra impreuna cu frecventa acesteia. Numele fisierului text este definit in segmentul de date.
segment data use32 class=data
    nume_fisier db "citire.txt", 0   ; numele fisierului care va fi deschis
    mod_acces db "r", 0             ; modul de deschidere a fisierului; r - pentru scriere. fisierul trebuie sa existe 
    descriptor dd -1            ; variabila in care vom salva descriptorul fisierului - necesar pentru a putea face referire la fisier
    format db "Cifra %c are frecventa cea mai mare din fisier ( %d )."
    caractere_citite dd 0              ; variabila in care vom salva numarul de caractere citit din fisier in etapa curenta
    cifra dd 0                      ; variabila in care vom salva cifra cu frecventa maxima
    contor dd 0                     ; variabila in care vom salva frecventa cifrei
    sir_cifre equ 10                ; lungimea sirului de frecvente
    frecvente resb sir_cifre        ; sirul in care vom stoca frecventele cifrelor
    len equ 100                     ; numarul maxim de elemente citite din fisier intr-o etapa
    buffer resb len                 ; sirul in care se va citi textul din fisier

; our code starts here
segment code use32 class=code
    start:
        ; apelam fopen pentru a deschide fisierul
        ; functia va returna in EAX descriptorul fisierului sau 0 in caz de eroare
        ; eax = fopen(nume_fisier, mod_acces)
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 2 * 4
        
        ; verificam daca functia fopen a creat cu succes fisierul (daca EAX != 0)
        cmp eax, 0                  
        je final
        
        mov [descriptor], eax   ; salvam valoarea returnata de fopen in variabila descriptor_fis
        
        mov ebx, 0
        bucla:
            ; citim o parte (100 caractere) din textul in fisierul deschis folosind functia fread
            ; eax = fread(buffer, 1, len, descriptor)
            push dword [descriptor]
            push dword len
            push dword 1
            push dword buffer
            call [fread]
            add esp, 4 * 4
        
                
            ; eax = numar de caractere / bytes citite
            cmp eax, 0          ; daca numarul de caractere citite este 0, am terminat de parcurs fisierul
            je cleanup

            mov [caractere_citite], eax        ; salvam numarul de caractere citie
               
            ; instructiunile pentru procesarea caracterelor citite in aceasta etapa incep aici
            mov esi, buffer
        verificare:
            lodsb ; al = caracter
            cmp al, 0 ; verificam daca sirul s-a terminat
            je done
            cmp al, '0' ; verificam daca este mai mare sau egal cu '0'
            jl verificare
            cmp al, '9' ; verificam daca este mai mic sau egal cu '9'
            jg verificare
            mov edx, 1 ; punem in edx valoarea 1
            add [frecvente + eax - '0'], edx ; crestem frecventa cifrei cu 1
            cmp [frecvente + eax - '0'], bl ; comparam frecventa cifrei cu frecventa maxima
            jl next ; daca este mai mica frecveta cifrei decat frecventa maxima sarim la next
            mov ebx, [frecvente + eax - '0'] ; daca este mai mare punem in ebx, frecventa cifrei
            mov [cifra], eax ; punem in variabila "cifra" cifra cu frecventa cea mai mare
            mov [contor], bl ; punem in variabila "contor" frecventa cifrei
            next:
            jmp verificare
        done:
            push edi           ; punem edi pe stiva pentru a nu pierde valoarea lui initiala
            lea edi,[buffer]   ; edi este inceputul buffer-ului
            xor eax,eax        ; punem in eax 0 
            mov ecx, len       ; punem in ecx lungimea pe care vrem sa o facem 0
            rep stosd          ; se repeta stosd pana cand segmentul de lungime len este umplut cu 0
            pop edi            ; aducem edi inapoi la valoarea lui initiala 
            
            ; reluam bucla pentru a citi alt bloc de caractere
            jmp bucla
        
      cleanup:
        ; apelam functia fclose pentru a inchide fisierul
        ; fclose(descriptor)
        push dword [descriptor]
        call [fclose]
        add esp, 4
        
      afisare:
        ; afisam cifra si frecventa corespunzatoare
        push dword [contor]
        push dword [cifra]
        push dword format
        call [printf]
        add esp, 3 * 4      
      final:  
        ; exit(0)
        push    dword 0      
        call    [exit]