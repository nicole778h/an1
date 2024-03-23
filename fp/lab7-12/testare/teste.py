from business.service_client import ServiceClient
from business.service_carte import ServiceCarte
from business.service_inchirieri import ServiceInchirieri
from domain.client import Client
from domain.carte import Carte
from domain.inchiriere import Inchiriere
from infrastructura.repo import Repo
from validare.validator_client import ValidatorClient
from validare.validator_carte import ValidatorCarte
from validare.validator_inchiriere import ValidatorInchirieri


class TesteClienti:
    def _init_(self):
        self.rClienti = Repo("test.json", Client)
        self.rCarti = Repo("test.json", Carte)
        self.rInchirieri = Repo("test.json", Inchiriere)
        self.vClient = ValidatorClient()
        self.vInchiriere = ValidatorInchirieri()
        self.vCarti = ValidatorCarte()
        self.bClienti = ServiceClient(self.rClienti, self.vClient)
        self.bCarti = ServiceCarte(self.rCarti, self.vCarti)
        self.bInchiriere = ServiceInchirieri(self.rInchirieri, self.rClienti, self.rCarti, self.vInchiriere)

    def run(self):
        self.__test_adaugare()
        self.__test_stergere()
        self.__test_modificare()
        print("Teste CLIENTI trecute cu succes")

    def __test_adaugare(self):
        self.rClienti.clear_all()
        assert len(self.bClienti.get_all()) == 0
        self.bClienti.adauga_client_service("Raul", "123123123")
        assert len(self.bClienti.get_all()) == 1

    def __test_stergere(self):
        self.rClienti.clear_all()
        self.bClienti.adauga_client_service("Raul", "123123123")
        assert len(self.bClienti.get_all()) == 1
        self.bInchiriere.sterge_client_service("0")
        assert len(self.bClienti.get_all()) == 0

    def __test_modificare(self):
        self.rClienti.clear_all()
        self.bClienti.adauga_client_service("Raul", "123123123")
        self.bClienti.modificare_client_service("0","nume","alex")
        self.bClienti.modificare_client_service("0", "cnp", "12903139210321")
        client = self.bClienti.get_by_id("0")
        assert client.get_nume() == "alex"
        assert client.get_cnp() == "12903139210321"