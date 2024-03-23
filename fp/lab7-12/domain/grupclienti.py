class GrupClienti:
    def __init__(self, client, nr_carti):

        self.__client = client
        self.__carti = nr_carti


    def get_client(self):
        return self.__client

    def get_nr_carti(self):
        return self.__carti

    def __str__(self):
        return f"ID:{self.__client.get_id()} NUME: {self.__client.get_nume()} CNP: {self.__client.get_cnp()} NR_CARTI: {self.__carti} "