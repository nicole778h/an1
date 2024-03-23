class Consola:
    def __init__(self, bs_clienti, bs_carti, bs_inchirieri):
        self.__bs_clienti = bs_clienti
        self.__bs_carti = bs_carti
        self.__bs_inchirieri = bs_inchirieri
        self.__instructiuni = {
            "adauga_client": self.__adaugare_client,
            "afisare_clienti": self.__afisare_clienti,
            "sterge_client": self.__stergere_client,
            "modifica_client": self.__modificare_client,
            "generare_clienti": self.__generare_client,
            "afisare_clienti_cresc_nume": self.__afisare_clienti_cresc_nume, #raport pt clienti cu carti dupa nume
            "afisare_clienti_descr_carti": self.__afisare_clienti_cresc_carti, #raport pt clienti dupa nr carti
            "afisare_clienti_activi": self.__afisare_clienti_activi, #raport pt 20% din cei mai activi clienti clienti



            "adauga_carte": self.__adaugare_carte,
            "afisare_carti": self.__afisare_carti,
            "sterge_carte": self.__stergere_carte,
            "modifica_carte": self.__modificare_carte,
            "afisare_carti_cresc": self.__afisare_carti_cresc_nume,
            "afisare_carti_desc": self.__afisare_carti_descr, # raport pt cele mai inchiriate carti

            "adauga_inchiriere": self.__adaugare_inchiriere,
            "afisare_inchirieri": self.__afisare_inchirieri,
            "sterge_inchiriere": self.__stergere_inchiriere,
            "modifica_inchiriere": self.__modificare_inchiriere,
            "returnare_inchiriere": self.__returnare_inchiriere

        }


    def run(self):
        while True:
            comenzi = input("introdu comanda>>> ")
            comenzi = comenzi.strip()
            comenzi = comenzi.split(";")
            for comanda in comenzi:
                # try:
                comanda = comanda.strip()
                comanda = comanda.split(" ")
                instructiune = comanda[0]
                params = comanda[1:]
                self.__instructiuni[instructiune](params)



    def __adaugare_client(self, params):
        nume = params[0]
        cnp = params[1]
        self.__bs_clienti.adaugare_client_service(nume, cnp)

    def __afisare_lista_indexata(self, lista): # afisare lista metoda recursiva
        n = 1
        if len(lista) == 0:
            return
        print(lista[0])
        self.__afisare_lista_indexata(lista[1:])

    def __afisare_clienti(self, params):
        clienti = self.__bs_clienti.get_all()
        # print("clienti:", clienti)
        self.__afisare_lista_indexata(clienti)

    def __stergere_client(self, params):
        id = params[0]
        self.__bs_inchirieri.stergere_client_service(id)

    def __modificare_client(self, params):
        id = params[0]
        camp = params[1]
        valoare = params[2]
        print("valorile ", id, " ", camp, " ", valoare)
        self.__bs_clienti.modificare_client_service(id, camp, valoare)

    def __adaugare_carte(self, params):
        titlu = params[0]
        descriere = params[1]
        autor = params[2]
        self.__bs_carti.adaugare_carte_service(titlu, descriere, autor)

    def __afisare_carti(self, params):
        carti = self.__bs_carti.get_all()
        self.__afisare_lista_indexata(carti)

    def __stergere_carte(self, params):
        id = params[0]
        self.__bs_inchirieri.stergere_carte_service(id)

    def __modificare_carte(self, params):
        id = params[0]
        camp = params[1]
        valoare = params[2]
        self.__bs_carti.modificare_carte_service(self, id, camp, valoare)

    def __adaugare_inchiriere(self, params):
        id_client = params[0]
        id_carte = params[1]
        self.__bs_inchirieri.adaugare_inchiriere_service(id_client, id_carte)

    def __afisare_inchirieri(self, params):
        inchirieri = self.__bs_inchirieri.get_all()
        self.__afisare_lista_indexata(inchirieri)

    def __stergere_inchiriere(self, params):
        id = params[0]
        self.__bs_inchirieri.sterge_inchiriere_service(id)

    def __modificare_inchiriere(self, params):
        id = params[0]
        camp = params[1]
        valoare = params[2]
        self.__bs_inchirieri.modificare_inchiriere_service(id, camp, valoare)

    def __generare_client(self, params): # generare clienti metoda recursiva
        numar = params[0]
        numar = int(numar)
        if len(params) == 0:
            return -1
        else:
            self.__bs_clienti.generare_client(numar)

    def __returnare_inchiriere(self, params):
        status = params[0]
        self.__bs_inchirieri.returnare_inchiriere_service(status)

    def __afisare_clienti_cresc_nume(self, params):
        lista = self.__bs_inchirieri.afisare_clienti_cresc_nume()
        self.__afisare_lista_indexata(lista)

    def __afisare_clienti_cresc_carti(self, params):
        lista = self.__bs_inchirieri.afisare_clienti_cresc_carti()
        lista_buna = []
        if len(lista) < 3:
            lista_buna.append(lista[0])
        else:
            lungime = len(lista) // 3
            lista_buna = lista[:lungime].copy()
        self.__afisare_lista_indexata(lista_buna)

    def __afisare_carti_descr(self, params):
        lista = self.__bs_inchirieri.afisare_carti_descr()
        self.__afisare_lista_indexata(lista)

    def __afisare_carti_cresc_nume(self, params):
        lista = self.__bs_inchirieri.afisare_carti_cresc_nume()
        self.__afisare_lista_indexata(lista)

    def __afisare_clienti_activi(self,params):
        lista = self.__bs_inchirieri.afisare_clienti_cresc_carti()
        lista_buna = []
        if len(lista) < 3:
            lista_buna.append(lista[0])
        else:
            lungime = len(lista) // 3
            lista_buna = lista[:lungime].copy()
        self.__afisare_lista_indexata(lista_buna)
