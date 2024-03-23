from business.service_client import ServiceClient
from business.service_carte import ServiceCarte
from business.service_inchirieri import ServiceInchirieri
from domain.client import Client
from domain.carte import Carte
from domain.inchiriere import Inchiriere
from infrastructura.repo import Repo
from prezentare.UI import Consola
from validare.validator_client import ValidatorClient
from validare.validator_carte import ValidatorCarte
from validare.validator_inchiriere import ValidatorInchirieri



def main():
    repo_client = Repo("clienti.json",Client)
    repo_carti = Repo("carte.json",Carte)
    repo_inchirieri = Repo("inchirieri.json",Inchiriere)
    validator_client = ValidatorClient()
    validator_carte = ValidatorCarte()
    validator_inchiriere = ValidatorInchirieri()
    bs_client = ServiceClient(validator_client, repo_client)
    bs_carte = ServiceCarte(validator_carte, repo_carti)
    bs_inchirieri = ServiceInchirieri(validator_inchiriere, repo_inchirieri, repo_client, repo_carti)
    consola = Consola(bs_client, bs_carte, bs_inchirieri)
    consola.run()


if __name__ == '__main__':
    main()
