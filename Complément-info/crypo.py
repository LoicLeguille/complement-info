def cesar(message_a_chiffrer,nombre_de_lettre_de_decalage):
    A=[0]*len(message_a_chiffrer)
    k=nombre_de_lettre_de_decalage
    for i in range(len(message_a_chiffrer)):
        if ord(message_a_chiffrer[i])>64 and ord(message_a_chiffrer[i])<91:
            A[i]=ord(message_a_chiffrer[i])-65
        if ord(message_a_chiffrer[i])>96 and ord(message_a_chiffrer[i])<123:
            A[i]=ord(message_a_chiffrer[i])-97
        A[i]=(k+A[i])%26
        if ord(message_a_chiffrer[i])>64 and ord(message_a_chiffrer[i])<91:
            A[i]=chr(A[i]+65)
        if ord(message_a_chiffrer[i])>96 and ord(message_a_chiffrer[i])<123:
            A[i]=chr(A[i]+95)
    return(A)
