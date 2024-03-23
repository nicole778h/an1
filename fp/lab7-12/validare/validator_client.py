from erori.validare_erori import ValidareErori


class ValidatorClient:

    def valideaza(self, client):
        id = client.get_id()
        nume = client.get_nume()
        cnp = client.get_cnp()
        eroare = ""
        if int(id) < 0:
            eroare += "id invalid\n"
        if nume == "":
            eroare += "nume invaalid\n"
        if cnp == "":
            eroare += "cnp invalid\n"
        if len(eroare) != 0:
            raise ValidareErori(eroare)
