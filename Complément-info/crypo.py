t=1
while t!=7:
    t=int(input('''\n       ===================
              MENU
       ===================
    1-codage césar
    2-codage affine
    3-codage vigenère
    4-décodage césar
    5-décodage affine
    6-décodage vigenère
    7-quitter le programme
    \nn° du choix : '''))
    if t<1 or t>7:
        print("\nce choix est impossible !")
        t=int(input('''\n        ===================
               MENU
        ===================
    1-codage césar
    2-codage affine
    3-codage vigenère
    4-décodage césar
    5-décodage affine
    6-décodage vigenère
    7-quitter le programme
    \nn° du choix : '''))



    if t==1:
        message_a_chiffrer=input('\nmessage a chiffrer: ')
        k=int(input('nombre de lettres de decalage: '))
        A=[0]*len(message_a_chiffrer)
        for i in range(len(message_a_chiffrer)):
            if ord(message_a_chiffrer[i])>64 and ord(message_a_chiffrer[i])<91:
                A[i]=ord(message_a_chiffrer[i])-65
            elif ord(message_a_chiffrer[i])>96 and ord(message_a_chiffrer[i])<123:
                A[i]=ord(message_a_chiffrer[i])-97
            elif ord(message_a_chiffrer[i])>223 and ord(message_a_chiffrer[i])<230:
                A[i]=0
            elif ord(message_a_chiffrer[i])==231:
                A[i]=2
            elif ord(message_a_chiffrer[i])>231 and ord(message_a_chiffrer[i])<236:
                A[i]=4
            elif ord(message_a_chiffrer[i])>236 and ord(message_a_chiffrer[i])<240:
                A[i]=8
            elif ord(message_a_chiffrer[i])>241 and ord(message_a_chiffrer[i])<246:
                A[i]=14
            elif ord(message_a_chiffrer[i])>248 and ord(message_a_chiffrer[i])<253:
                A[i]=20
            else:
                A[i]=message_a_chiffrer[i]
            if A[i]!=message_a_chiffrer[i]:
                A[i]=(k+A[i])%26
                if ord(message_a_chiffrer[i])>64 and ord(message_a_chiffrer[i])<91 :
                    A[i]=chr(A[i]+65)
                if (ord(message_a_chiffrer[i])>96 and ord(message_a_chiffrer[i])<123) or ord(message_a_chiffrer[i])>200:
                    A[i]=chr(A[i]+97)
        A=''.join(A)
        print('message codé:',A)



    if t==2:
        print('\nfonction affine y = a*x+b  (le coeff a doit etre premier avec 26)\n' ) 
        message_a_chiffrer=input('message à chiffrer: ')
        c=0
        while c!=1:
            a=int(input('valeur du coefficient a: '))
            b=int(input('valeur du coefficient b: '))
            c=max(a,b)
            d=min(a,b)
            while d!=0 :
                r=c-d*int(c/d)
                c=d
                d=r
            if c!=1:
                print("\na doit etre premier avec 26 (nombres de lettres de l'alphabet)\n")
        A=[0]*len(message_a_chiffrer)
        for i in range(len(message_a_chiffrer)) :
            if ord(message_a_chiffrer[i])>64 and ord(message_a_chiffrer[i])<91:
                A[i]=ord(message_a_chiffrer[i])-65
            elif ord(message_a_chiffrer[i])>96 and ord(message_a_chiffrer[i])<123:
                A[i]=ord(message_a_chiffrer[i])-97
            elif ord(message_a_chiffrer[i])>223 and ord(message_a_chiffrer[i])<230:
                A[i]=0
            elif ord(message_a_chiffrer[i])==231:
                A[i]=2
            elif ord(message_a_chiffrer[i])>231 and ord(message_a_chiffrer[i])<236:
                A[i]=4
            elif ord(message_a_chiffrer[i])>236 and ord(message_a_chiffrer[i])<240:
                A[i]=8
            elif ord(message_a_chiffrer[i])>241 and ord(message_a_chiffrer[i])<246:
                A[i]=14
            elif ord(message_a_chiffrer[i])>248 and ord(message_a_chiffrer[i])<253:
                A[i]=20
            else:
                A[i]=message_a_chiffrer[i]
            if A[i]!=message_a_chiffrer[i]:
                A[i]=((A[i]*a)+b)%26
                if ord(message_a_chiffrer[i])>64 and ord(message_a_chiffrer[i])<91:
                    A[i]=chr(A[i]+65)
                if (ord(message_a_chiffrer[i])>96 and ord(message_a_chiffrer[i])<123) or ord(message_a_chiffrer[i])>200:
                    A[i]=chr(A[i]+97)
        A=''.join(A)
        print('message codé:',A)



    if t==3:
        message_a_chiffrer=input('\nmessage à chiffrer: ')
        cle=input('clé de codage: ')
        A=[0]*max(len(cle),len(message_a_chiffrer))
        B=[0]*len(message_a_chiffrer)
        for k in range(len(A)):
            if ord(cle[k%len(cle)])>64 and ord(cle[k%len(cle)])<91:
                A[k]=ord(cle[k%len(cle)])-65
            if ord(cle[k%len(cle)])>96 and ord(cle[k%len(cle)])<123:
                A[k]=ord(cle[k%len(cle)])-97
            if ord(message_a_chiffrer[i])>223 and ord(message_a_chiffrer[i])<230:
                A[i]=0
            if ord(message_a_chiffrer[i])==231:
                A[i]=2
            if ord(message_a_chiffrer[i])>231 and ord(message_a_chiffrer[i])<236:
                A[i]=4
            if ord(message_a_chiffrer[i])>236 and ord(message_a_chiffrer[i])<240:
                A[i]=8
            if ord(message_a_chiffrer[i])>241 and ord(message_a_chiffrer[i])<246:
                A[i]=14
            if ord(message_a_chiffrer[i])>248 and ord(message_a_chiffrer[i])<253:
                A[i]=20
        for i in range(len(message_a_chiffrer)) :
            if ord(message_a_chiffrer[i])>64 and ord(message_a_chiffrer[i])<91:
                B[i]=ord(message_a_chiffrer[i])-65
            elif ord(message_a_chiffrer[i])>96 and ord(message_a_chiffrer[i])<123:
                B[i]=ord(message_a_chiffrer[i])-97
            elif ord(message_a_chiffrer[i])>223 and ord(message_a_chiffrer[i])<230:
                A[i]=0
            elif ord(message_a_chiffrer[i])==231:
                A[i]=2
            elif ord(message_a_chiffrer[i])>231 and ord(message_a_chiffrer[i])<236:
                A[i]=4
            elif ord(message_a_chiffrer[i])>236 and ord(message_a_chiffrer[i])<240:
                A[i]=8
            elif ord(message_a_chiffrer[i])>241 and ord(message_a_chiffrer[i])<246:
                A[i]=14
            elif ord(message_a_chiffrer[i])>248 and ord(message_a_chiffrer[i])<253:
                A[i]=20
            else:
                B[i]=message_a_chiffrer[i]
            if B[i]!=message_a_chiffrer[i]:
                B[i]=(abs(A[i]-B[i])+B[i])%26
                if ord(message_a_chiffrer[i])>64 and ord(message_a_chiffrer[i])<91:
                    B[i]=chr(B[i]+65)
                if (ord(message_a_chiffrer[i])>96 and ord(message_a_chiffrer[i])<123) or ord(message_a_chiffrer[i])>200:
                    B[i]=chr(B[i]+97)
        B=''.join(B)
        print('message codé:',B)



    if t==4:
        message_a_dechiffrer=input('\nmessage à déchiffrer: ')
        B=[0]*len(message_a_dechiffrer)
        print('décalage de','|','message décodé\n')
        for k in range(1,26):
            for i in range(len(message_a_dechiffrer)):
                if ord(message_a_dechiffrer[i])>64 and ord(message_a_dechiffrer[i])<91:
                    B[i]=ord(message_a_dechiffrer[i])-65
                elif ord(message_a_dechiffrer[i])>96 and ord(message_a_dechiffrer[i])<123:
                    B[i]=ord(message_a_dechiffrer[i])-97
                else:
                    B[i]=message_a_dechiffrer[i]
                if B[i]!=message_a_dechiffrer[i]:
                    B[i]=((26-k)+B[i])%26
                if ord(message_a_dechiffrer[i])>64 and ord(message_a_dechiffrer[i])<91:
                    B[i]=chr(B[i]+65)
                elif ord(message_a_dechiffrer[i])>96 and ord(message_a_dechiffrer[i])<123:
                    B[i]=chr(B[i]+97)
            if k<10:
                print('        ',k,' :',''.join(B))
            else:
                print('        ',k,':',''.join(B))


                
    if t==5:
        message_a_dechiffrer=input('\nmessage à déchiffrer: ')
        B=[0]*len(message_a_dechiffrer)
        print('coefficients a/b','|','message décodé\n')
        a=[1,3,5,7,9,11,15,17,19,21,23,25]
        z=[1,9,21,15,3,19,7,23,11,5,17,25]
        for k in range(len(z)):
            for b in range(1,26):
                for i in range(len(message_a_dechiffrer)):
                    if ord(message_a_dechiffrer[i])>64 and ord(message_a_dechiffrer[i])<91:
                        B[i]=ord(message_a_dechiffrer[i])-65
                    elif ord(message_a_dechiffrer[i])>96 and ord(message_a_dechiffrer[i])<123:
                        B[i]=ord(message_a_dechiffrer[i])-97
                    else:
                        B[i]=message_a_dechiffrer[i]
                    if B[i]!=message_a_dechiffrer[i]:
                        B[i]=(z[k]*(B[i]-b))%26
                    if ord(message_a_dechiffrer[i])>64 and ord(message_a_dechiffrer[i])<91:
                        B[i]=chr(B[i]+65)
                    if ord(message_a_dechiffrer[i])>96 and ord(message_a_dechiffrer[i])<123:
                        B[i]=chr(B[i]+97)
                if a[k]<10 and b<10:
                    print('        ',a[k],'/',b,'  :',''.join(B))
                if a[k]<10 and b>10:
                    print('        ',a[k],'/',b,' :',''.join(B))
                if a[k]>10 and b<10:
                    print('        ',a[k],'/',b,' :',''.join(B))
                if a[k]>10 and b>10:
                    print('        ',a[k],'/',b,':',''.join(B))



    if t==6:
        message_a_dechiffrer=input('\nmessage à déchiffrer: ')
        cle=input('clé de codage: ')
        A=[0]*max(len(cle),len(message_a_dechiffrer))
        B=[0]*len(message_a_dechiffrer)
        for k in range(len(A)):
            if ord(cle[k%len(cle)])>64 and ord(cle[k%len(cle)])<91:
                A[k]=ord(cle[k%len(cle)])-65
            if ord(cle[k%len(cle)])>96 and ord(cle[k%len(cle)])<123:
                A[k]=ord(cle[k%len(cle)])-97
        for i in range(len(message_a_dechiffrer)) :
            if ord(message_a_dechiffrer[i])>64 and ord(message_a_dechiffrer[i])<91:
                B[i]=ord(message_a_dechiffrer[i])-65
            elif ord(message_a_dechiffrer[i])>96 and ord(message_a_dechiffrer[i])<123:
                B[i]=ord(message_a_dechiffrer[i])-97
            else:
                B[i]=message_a_dechiffrer[i]
            if B[i]!=message_a_dechiffrer[i]:
                   B[i]=(B[i]-abs(A[i]-B[i]))%26
            if ord(message_a_dechiffrer[i])>64 and ord(message_a_dechiffrer[i])<91:
                B[i]=chr(B[i]+65)
            if ord(message_a_dechiffrer[i])>96 and ord(message_a_dechiffrer[i])<123:
                B[i]=chr(B[i]+97)
        B=''.join(B)
        print('message décodé:',B)


    
                
