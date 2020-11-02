from datetime import datetime

candidatos = []
votos = []
nulos = []


class Candidato:

    def __init__(self, nome, partido, numero):
        self.__nome = nome
        self.__partido = partido
        self.__numero = numero
    
    @property
    def get_nome(self):
        return self.__nome
    
    @property
    def get_partido(self):
        return self.__partido
    
    @property
    def get_numero(self):
        return self.__numero
    

class Voto:

    def __init__(self, cpf_eleitor, numero_candidato):
        self.__cpf_eleitor = cpf_eleitor
        self.__numero_candidato = numero_candidato
        self.hora = datetime.now().strftime("%H:%M:%S")
    
    @property
    def get_cpf_eleitor(self):
        return self.__cpf_eleitor
    
    @property
    def get_numero_candidato(self):
        return self.__numero_candidato


# Funções a parte.

def votar(cpf, numero):
    var = []
    for x in candidatos:
        var.append(x.get_numero)
    
    if numero in var:
        voto = Voto(cpf, numero)
        votos.append(voto)
    else:
        nulos.append('voto_nulo')

def contar_voto(numero_candidato):
    voto = 0
    for x in votos:
        if x.get_numero_candidato == numero_candidato:
            voto += 1
    return voto

def contar_nulo():
    return len(nulos)


# Testando

c1 = Candidato('Zeraldo', 'PT', 1234)
candidatos.append(c1)

c2 = Candidato('Gustavo', 'PSDB', 3210)
candidatos.append(c2)

c3 = Candidato('Joao Vitor', 'PSOL', 4231)
candidatos.append(c3)

votar(123456789, 1234)
votar(67854312609, 3210)
votar(381278427893578941, 120389120391)
votar(12312387123, 4231)

for candidato in candidatos:
    print(f'O candidato {candidato.get_nome} conseguiu {contar_voto(candidato.get_numero)} votos')
print(f'Houveram {contar_nulo()} votos nulos.')
