class GrupCarti:
    def __init__(self, carte, nr_inchirieri):
        self.__nr_inchirieri = nr_inchirieri
        self.__carte = carte

    def __str__(self):
        return f"ID: {self.__carte.get_id()} TITLU: {self.__carte.get_titlu()} DESCRIERE: {self.__carte.get_descriere()} AUTOR: {self.__carte.get_autor()} INCHIRIERI: {self.__nr_inchirieri}"