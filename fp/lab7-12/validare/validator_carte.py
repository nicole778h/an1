from erori.validare_erori import ValidareErori


class ValidatorCarte:
    def valideaza(self, carte):
        id = carte.get_id()
        titlu = carte.get_titlu()
        descriere = carte.get_descriere()
        autor = carte.get_autor()
        eroare=""
        if int(id)<0:
            eroare+="id invalid\n"
        if titlu=="":
            eroare+="titlu invalid\n"
        if descriere=="":
            eroare+="descriere invalida\n"
        if autor=="":
            eroare+="autor invalid\n"
        if len(eroare)!=0:
            raise ValidareErori(eroare)