class Carte:

    def __init__(self, *args):
        if len(args) == 4:
            self.__id = args[0]
            self.__titlu = args[1]
            self.__descriere = args[2]
            self.__autor = args[3]
            self.__sters = False
        if len(args) == 1:
            # print(args)
            self.__id = args[0]["carte_id"]
            self.__titlu = args[0]["carte_titlu"]
            self.__descriere = args[0]["carte_descriere"]
            self.__autor = args[0]["carte_autor"]
            self.__sters = args[0]["carte_sters"]

    def get_id(self):
        return self.__id

    def get_titlu(self):
        return self.__titlu

    def get_descriere(self):
        return self.__descriere

    def get_autor(self):
        return self.__autor

    def is_sters(self):
        return self.__sters

    def set_titlu(self, titlu_nou):
        self.__titlu = titlu_nou

    def set_autor(self,autor_nou):
        self.__autor = autor_nou

    def set_sters(self, stare):
        self.__sters = stare

    def set_descriere(self, descriere_noua):
        self.__descriere = descriere_noua

    def to_dict(self):
        dict={
            "carte_id":self.__id,
            "carte_titlu":self.__titlu,
            "carte_descriere":self.__descriere,
            "carte_autor":self.__autor,
            "carte_sters":self.__sters
        }
        return dict

    def __eq__(self, other):
        return self.__id == other.get_id

    def __str__(self):
        return f"ID:{self.__id} TITLU: {self.__titlu} DESCRIERE: {self.__descriere} AUTOR: {self.__autor}"