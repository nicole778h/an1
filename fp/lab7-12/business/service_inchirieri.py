from business.functii import find_id, mergesort, bingosort
from domain.grupclienti import GrupClienti
from domain.grupcarti import GrupCarti
from domain.inchiriere import Inchiriere


class ServiceInchirieri():
    def __init__(self, validator_inchiriere, repo_inchiriere, repo_client, repo_carte):
        self.__validator_inchiriere = validator_inchiriere
        self.__repo_inchiriere = repo_inchiriere
        self.__repo_client = repo_client
        self.__repo_carte = repo_carte

    def adaugare_inchiriere_service(self, id_client, id_carte):
        lista = self.__repo_inchiriere.get_all()
        id = find_id(lista)
        client = self.__repo_client.get_dupa_id(id_client)
        carte = self.__repo_carte.get_dupa_id(id_carte)
        inchiriere = Inchiriere(id, client, carte)
        self.__validator_inchiriere.valideaza(inchiriere)
        self.__repo_inchiriere.add_to_dict(inchiriere)

    def modificare_inchiriere_service(self, id, camp, valoare):
        inchiriere = self.__repo_inchiriere.get_dupa_id(id)
        # print(inchiriere)
        # inchiriere_modificata = ""
        if camp == "client":
            inchiriere_modificata = Inchiriere(id, self.__repo_client.get_dupa_id(valoare), inchiriere.get_carte(), inchiriere.get_status())
            # print("1")
        elif camp == "carte":
            inchiriere_modificata = Inchiriere(id, inchiriere.get_client(), self.__repo_carte.get_dupa_id(valoare), inchiriere.get_status())
            # print(inchiriere_modificata)
        elif camp == "status":
            inchiriere_modificata = Inchiriere(id, inchiriere.get_client(), inchiriere.get_carte(), valoare)
        # print(inchiriere_modificata)
        self.__validator_inchiriere.valideaza(inchiriere_modificata)
        self.__repo_inchiriere.update(inchiriere_modificata)


    def modificare_inchiriere_service_extended(self, id, camp, valoare):
        inchiriere = self.__repo_inchiriere.get_dupa_id_extended(id)
        inchiriere_modificata = ""
        if camp == "client":
            inchiriere_modificata = Inchiriere(id, valoare, inchiriere.get_carte(), inchiriere.get_status())
        elif camp == "carte":
            inchiriere_modificata = Inchiriere(id, inchiriere.get_client(), valoare, inchiriere.get_status())
        elif camp == "status":
            inchiriere_modificata = Inchiriere(id, inchiriere.get_client(), inchiriere.get_carte(), valoare)
        self.__validator_inchiriere.valideaza(inchiriere_modificata)
        self.__repo_inchiriere.update(inchiriere_modificata)

    def link(self):
        lista = self.__repo_inchiriere.get_all_extended()
        for inchiriere in lista:

            self.modificare_inchiriere_service_extended(inchiriere.get_id(), "carte", inchiriere.get_carte().get_id())
            self.modificare_inchiriere_service_extended(inchiriere.get_id(), "client", inchiriere.get_client().get_id())

    def get_all(self):
        lista = self.__repo_inchiriere.get_all()
        return lista

    def sterge_inchiriere_service(self, id):
        self.__repo_inchiriere.delete_dupa_id(id)

    def stergere_client_service(self, id):
        lista = self.__repo_inchiriere.get_all()
        for inchiriere in lista:
            if inchiriere.get_client().get_id() == id:
                self.__repo_inchiriere.delete_dupa_id(inchiriere.get_id())
        self.__repo_client.delete_dupa_id(id)

    def stergere_carte_service(self, id):
        lista = self.__repo_inchiriere.get_all()
        for inchiriere in lista:
            if inchiriere.get_carte().get_id() == id:
                self.__repo_inchiriere.delete_dupa_id(inchiriere.get_id())
        self.__repo_carte.delete_dupa_id(id)

    def returnare_inchiriere_service(self, inchiriere_id):
        inchiriere = self.__repo_inchiriere.get_dupa_id(inchiriere_id)
        inchiriere.set_status(0)

    def get_client_nr_inchirieri(self, id):
        nr = 0
        lista = self.get_all()
        for inchiriere in lista:
            if inchiriere.get_client().get_id() == id:
                nr += 1
        return nr

    def get_carte_nr_inchirieri(self, id):
        nr = 0
        lista = self.get_all()
        for inchiriere in lista:
            if inchiriere.get_carte().get_id() == id:
                nr += 1
        return nr


    def afisare_clienti_cresc_nume(self):
        lista = self.__repo_client.get_all()
        lista = sorted(lista, key=lambda client: (client.get_nume(), -1 * self.get_client_nr_inchirieri(client.get_id())))
        # print(lista)
        grup = []
        for client in lista:
            grup.append(GrupClienti(client, self.get_client_nr_inchirieri(client.get_id())))
        return grup


    def afisare_clienti_cresc_carti(self):
        lista = self.__repo_client.get_all()
        lista = mergesort(lista, key=lambda client: (-1 * self.get_client_nr_inchirieri(client.get_id())))
        # print(lista)
        grup = []
        for client in lista:
            grup.append(GrupClienti(client, self.get_client_nr_inchirieri(client.get_id())))
        return grup

    def afisare_carti_descr(self):
        lista = self.__repo_carte.get_all()
        lista = bingosort(lista,
                                key=lambda carte: (-1 * self.get_carte_nr_inchirieri(carte.get_id())))
        # print(lista)
        # for x in lista:
        #     print(x)
        grup = []
        for carte in lista:
            grup.append(GrupCarti(carte, self.get_carte_nr_inchirieri(carte.get_id())))
        return grup

    def afisare_carti_cresc_nume(self):
        lista = self.__repo_carte.get_all()
        lista = mergesort(lista, key=lambda carte: (carte.get_titlu()))

        return lista

