from business.functii import find_id
from domain.carte import Carte


class ServiceCarte:
    def __init__(self, validator_carte, repo_carte):
        self.__validator_carte = validator_carte
        self.__repo_carte = repo_carte

    def adaugare_carte_service(self, titlu, descriere, autor):
        lista = self.__repo_carte.get_all()
        id = find_id(lista)
        carte = Carte(id, titlu, descriere, autor)

        self.__validator_carte.valideaza(carte)
        self.__repo_carte.add_to_dict(carte)

    def modificare_carte_service(self, id, camp, valoare):
        carte = self.__repo_carte.get_dupa_id()
        carte_modificat=""
        if camp=="titlu":
            carte_modificat= Carte(id, valoare, carte.get_autor(), carte.get_descriere())
        elif camp == "autor":
            carte_modificat= Carte(id, carte.get_titlu(), valoare, carte.get_descriere())
        elif camp == "descriere":
            carte_modificat= Carte(id, carte.get_titlu(), carte.get_descriere())
        self.__validator_carte.valideaza(carte_modificat)
        self.__repo_carte.update(carte_modificat)

    def get_all(self):
        lista = self.__repo_carte.get_all()
        return lista
