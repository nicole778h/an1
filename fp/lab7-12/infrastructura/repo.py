import json

from erori.repo_erori import RepoErori


class Repo:
    def __init__(self, fisier, tip):
        self.__dict = {}
        self.__fisier = fisier
        self.__tip = tip
        self.incarcare_date()

    def add_to_dict(self, entitate):
        if entitate.get_id() in self.__dict:
            raise RepoErori('Id-ul este deja folosit!')
        self.__dict[entitate.get_id()] = entitate
        self.salvare_date()

    def get_dupa_id(self, id):
        """
        Functia returneaza o entitate dupa id din dictionar
        :param id:
        :return:
        """
        if id not in self.__dict:
            raise RepoErori('Entitate inexistenta!')
        if self.__dict[id].is_sters():
            raise RepoErori('Entitate inexistenta!')
        return self.__dict[id]

    def get_dupa_id_extended(self, id):
        """
        Functia returneaza o entitate dupa id din dictionar
        :param id:
        :return:
        """
        if id not in self.__dict:
            raise RepoErori('Entitate inexistenta!')
        return self.__dict[id]

    def get_nr(self):
        """
        Functia returneaza numarul de enitati dintr un dictionar
        :return:
        """
        x = 0
        for id in self.__dict.keys():
            if not self.__dict[id].is_sters():
                x = x + 1
        return x

    def get_all(self):
        """
        Functia returneaza lista cu toate entitatile din dictionar
        :return:
        """
        lista = []
        for key in self.__dict:
            if not self.__dict[key].is_sters():
                lista.append(self.__dict[key])
        return lista

    def get_all_extended(self):
        """
        Functia returneaza lista cu toate entitatile din dictionar
        :return:
        """
        lista = []
        for key in self.__dict:
            lista.append(self.__dict[key])
        return lista

    def delete_dupa_id(self, id):
        if id not in self.__dict:
            raise RepoErori('Entitate inexistenta!')
        if not self.__dict[id].is_sters():
            self.__dict.pop(id)
            self.salvare_date()



    def update(self, entitate):
        id = entitate.get_id()
        self.__dict[id] = entitate
        self.salvare_date()

    def salvare_date(self):
        # dict_save = {x.__dict__ for x in self.__dict.values()}
        dict_save = {}
        for entity in self.__dict:
            obiect = self.__dict[entity].to_dict()

            dict_save[entity] = obiect

        #print(dict_save)

        with open(self.__fisier, "w") as outfile:
            json.dump(dict_save, outfile)

    def incarcare_date(self):
        try:
            with open(self.__fisier, 'r') as openfile:
                dict = json.load(openfile)
            #print(dict)
            for key in dict:
                self.__dict[key] = self.__tip(dict[key])
        except:
            pass