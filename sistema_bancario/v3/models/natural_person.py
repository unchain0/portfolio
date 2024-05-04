from abc import ABC
from datetime import date


class NaturalPerson(ABC):
    def __init__(self, cpf: str, name: str, birth_date: date):
        self.__cpf = cpf
        self.__name = name
        self.__birth_date = birth_date

    @property
    def cpf(self):
        return self.__cpf

    @property
    def name(self):
        return self.__name

    @property
    def birth_date(self):
        return self.__birth_date
