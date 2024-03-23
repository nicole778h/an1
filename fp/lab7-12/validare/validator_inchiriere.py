from erori.validare_erori import ValidareErori


class ValidatorInchirieri:
    def valideaza(self, inchirieri):
        # print(inchirieri)
        id = inchirieri.get_id()
        client = inchirieri.get_client()
        carte = inchirieri.get_carte()
        status = inchirieri.get_status()
        eroare = ""
        if int(id) < 0:
            eroare += "id invalid\n"
        if client.get_id() == "":
            eroare += "client invalid\n"
        if carte.get_id() == "":
            eroare += "carte invalid\n"
        if status == "":
            eroare += "status invalida\n"
        if len(eroare) != 0:
            raise ValidareErori(eroare)
