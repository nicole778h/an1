class Client:
    # def __init__(self, id, nume, cnp):
    #     self.__id = id
    #     self.__nume = nume
    #     self.__cnp = cnp
    #     self.__sters = False

    def __init__(self, *args):
        if len(args) == 3:
            self.__id = args[0]
            self.__nume = args[1]
            self.__cnp = args[2]
            self.__sters = False
        if len(args) == 1:
            # print(args)
            self.__id = args[0]["client_id"]
            self.__nume = args[0]["client_nume"]
            self.__cnp = args[0]["client_cnp"]
            self.__sters = args[0]["client_sters"]

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp

    def is_sters(self):
        return self.__sters

    def set_nume(self, nume_nou):
        self.__nume = nume_nou

    def set_cnp(self, cnp_nou):
        self.__cnp = cnp_nou

    def set_sters(self, stare):
        self.__sters = stare

    def to_dict(self):
        dict = {
            "client_id": self.__id,
            "client_nume": self.__nume,
            "client_cnp": self.__cnp,
            "client_sters": self.__sters
        }
        return dict

    def __eq__(self, other):
        return self.__id == other.get_id()

    def __str__(self):
        return f"ID:{self.__id} NUME: {self.__nume} CNP: {self.__cnp}"
