import json
from abc import abstractmethod

from contato import Contato
from contato_dao import ContatoDao


class ContatoDaoJson(ContatoDao):
    @abstractmethod
    def buscar_todos(self, caminho):
        contatos = []
        with open(caminho, mode='r') as arquivo:
            contatos_json = json.load(arquivo)

            for contato in contatos_json:
                c = Contato(**contato)
                contatos.append(c)
        return contatos

    @abstractmethod
    def salvar(self, contatos, caminho):
        with open(caminho, mode='w') as arquivo:
            json.dump(contatos, arquivo, default=lambda objeto: objeto.__dict__)
