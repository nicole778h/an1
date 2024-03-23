from domain.client import Client
from domain.carte import Carte


class Inchiriere:



    def __init__(self, *args):
        if len(args) == 3:
            self.__id = args[0]
            self.__client = args[1]
            self.__carte = args[2]
            self.__status = 1
            self.__sters = False
        elif len(args) == 4:
            self.__id = args[0]
            self.__client = args[1]
            self.__carte = args[2]
            self.__status = args[3]
            self.__sters = False
            # print("init")
        elif len(args) == 1:
            # print(args)
            self.__id = args[0]["inchiriere_id"]
            self.__client = Client(args[0]["inchiriere_client"])
            self.__carte = Carte(args[0]["inchiriere_carte"])
            self.__status = args[0]["inchiriere_status"]
            self.__sters = args[0]["inchiriere_sters"]


    def get_id(self):
        return self.__id

    def get_client(self):
        return self.__client

    def get_carte(self):
        return self.__carte

    def get_status(self):
        return self.__status

    def is_sters(self):
        return self.__sters

    def set_client(self, client_nou):
        self.__client = client_nou

    def set_carte(self, carte_nou):
        self.__carte = carte_nou

    def set_status(self, status_nou):
        self.__status = status_nou

    def set_sters(self, status):
        self.__sters = status

    def to_dict(self):
        dict={
            "inchiriere_id":self.__id,
            "inchiriere_client":self.__client.to_dict(),
            "inchiriere_carte":self.__carte.to_dict(),
            "inchiriere_status":self.__status,
            "inchiriere_sters":self.__sters

        }
        return dict

    def __eq__(self, other):
        return self.__id == other.get_id

    def __str__(self):
        return f"ID: {self.__id} ID_CLIENT: {self.__client.get_id()} ID_CARTE: {self.__carte.get_id()} STATUS: {self.__status}"
