#Job10

def verif(chiffre):
    if chiffre >= 0:
        print("c'est OK")
    else:
        print("HEUUU NON ! \nC'est pas bon comme chiffre ou nombre gros rageux !!!")
        return
    if chiffre % 2 == 0:
        print(f"le chiffre {chiffre} est bien paire\n ")
    else:
        print(f"le chiffre {chiffre} est bien impaire\n ")  

verif(-1)
verif(1)
verif(0)
verif(27)
verif(58)
verif(-12)