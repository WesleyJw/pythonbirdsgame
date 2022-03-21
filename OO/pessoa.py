class Pessoa:
    #atributo default ou atributo de classe
    olhos = 2
    def __init__(self, *filhos, nome=None):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá meu nome é: {self.nome}."

    #Metodo de Classe: esse metodo independe tanto da classe quanto do objeto, nao recebe parametros
    #inserindo um decorator
    @staticmethod         #metodo estatico
    def metodo_estatico():
        return 21

    #Decoretor de classe
    @classmethod         #utilizado quando se quer acessar dados da propria classe
    def nome_e_atributos_de_classe(cls):   #cls aponta para a classe Pessoa
        return  f'{cls} - Olhos {cls.olhos}'

    #Composicao: É a maneira na qual a gente agrega objetos de diferentes tipos para executar determinado codigo
    # Separando responsabilidades o codigo de cada classe fica mais simples, apesar de aumentar a complexidade
    # do codigo, pois temos difernetes objetos se comunicando para executar uma mesma coisa.

    #Heranca: é uma forma de reutilizar codigos de acordo com uma classe pre-existente. forma de cestabelecer HERANCA
    #A heranca herda todos os atributos da classe pai

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    #sobrescrita de atributo na classe Mutante
    olhos = 3
    #Sobrescrita de metodo
    def cumprimentar(self):
        #Acessar recusivamente o cumprimentar da classe pai
        cumprimentar_classe_pai = super(Mutante, self).cumprimentar()
        return f"{cumprimentar_classe_pai}, eu sou mutante."




if __name__ == '__main__':
    wesley = Pessoa(nome = "Wesley")
    jose = Pessoa(wesley, nome = "Jose")
    print(jose.cumprimentar())

    for filho in jose.filhos:
        print(filho.nome)

    print(Pessoa.nome_e_atributos_de_classe(), jose.nome_e_atributos_de_classe())

    # Sobrescrita de atributos em heranças
    print(wesley.olhos)
    wesley = Mutante(nome="Wesley")
    jose = Pessoa(wesley, nome="Jose")
    print(wesley.olhos)
    print(jose.olhos)
    print(wesley.cumprimentar())
    print(jose.cumprimentar())




