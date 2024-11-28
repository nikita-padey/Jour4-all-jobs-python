#Job9

note1 = int(input("donne ta 1 er note : "))
note2 = int(input("donne ta 1 er note : "))
note3 = int(input("donne ta 1 er note : "))

def moyenne(note1,note2,note3):
    moyenne_etudiant = (note1 + note2 + note3)/3
    if 20 >= moyenne_etudiant >= 15:
        print("Très bon élève")
    elif 15 > moyenne_etudiant >= 11:
        print("Bon élève")
    elif 11 > moyenne_etudiant >= 8:
        print("Élève moyen")
    else:
        print("Élève devant faire des efforts")
    return (note1 + note2 + note3)/3

print("ta moyenne est de ", moyenne(note1,note2,note3))