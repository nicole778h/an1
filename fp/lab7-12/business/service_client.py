import random

from business.functii import find_id
from domain.client import Client


class ServiceClient:
    def __init__(self, validator_client, repo_clienti):
        self.__validator_client = validator_client
        self.__repo_clienti = repo_clienti

    def adaugare_client_service(self, nume, cnp):
        lista = self.__repo_clienti.get_all()
        id = find_id(lista)
        client = Client(id, nume, cnp)
        self.__validator_client.valideaza(client)
        self.__repo_clienti.add_to_dict(client)

    def modificare_client_service(self, id, camp, valoare):
        client = self.__repo_clienti.get_dupa_id(id)
        client_modificat = ""
        if camp == "nume":
            client_modificat = Client(id, valoare, client.get_cnp())
        elif camp == "cnp":
            client_modificat = Client(id, client.get_nume(), valoare)
        self.__validator_client.valideaza(client_modificat)
        self.__repo_clienti.update(client_modificat)

    def get_all(self):
        lista = self.__repo_clienti.get_all()
        return lista

    def generare_client(self, nr):#recursiv
        if nr>0:
            lista = ["ana", "nicole", "raul", "andrei", "dragos", "giulia", "maria", "ileana"]
            self.adaugare_client_service(random.choice(lista),random.randint(10000000000000, 99999999999999999999))
            self.generare_client(nr-1)