# TEMA 1 ISC -> ANCA-MARIA COLACEL

**Tema contine 3 taskuri. Le voi detalia pe fiecare in parte.**

## TASK1 - CRYPTO-ATTACK
In vederea rezolvarii acestui exercitiu a fost necesara completarea scriptului pus la dispozitie in arhiva.
Am inceput cu hinturile puse la dispozitie in cerinta si decodand din base64 KLT vahlxg vbiaxkmxqm tmmtvd am vazut ca se foloseste RSA chosen chiper attack. Celalalt nu era util :)
Am incercat sa decodez message.txt din b64 si am obtinut un json cu 3 campuri, n, e si flag, astfel am format chiper_dash-ul necesar algoritmului in urma aplicarii formulei. M-am gandit ca formatul in care trebuie trimise informatiile la server este tot json astfel ca formez noul json folosind chiper_dash-ul, l-am encodat si l-am trimis la server. Salvez raspunsul de la server, folosesc decode-unicode si apoi fac conversie din string in numar pt ca potrivit algoritmului trebuie sa impart la numarul random. Dupa ce fac impartirea practic obtin flagul dar in format numeric asa ca il convertesc in string si il printez. 
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

  3) Dupa ce ma uit prin fisiere observ ca de interes este fisierul robo-sudo acesta avand userul zboss

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

   
   
    
 
 , 

